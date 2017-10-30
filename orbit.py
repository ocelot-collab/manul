"""
Sergey Tomin. XFEL/DESY, 2017.
"""
from threading import Thread, Event
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore
import numpy as np
from ocelot import *

from ocelot.cpbd.track import *
import time
from ocelot.cpbd.orbit_correction import NewOrbit, OrbitSVD
from ocelot.cpbd.response_matrix import *
from devices import *
from golden_orbit import GoldenOrbit
from adaptive_feedback import UIAFeedBack
from ocelot.optimizer.mint.xfel_interface import *

class ResponseMatrixCalculator(Thread):
    """
    Wrap for ResponseMatrix class. Allow to calculate response matrices (ORM and DRM) in different thread
    """

    def __init__(self, rm, drm):
        super(ResponseMatrixCalculator, self).__init__()
        self.rm = rm
        self.drm = drm
        self.do_DRM_calc = True
        self.tw_init = None
        self.rm_filename = None
        self.drm_filename = None

    def run(self):
        self.rm.calculate(tw_init=self.tw_init)
        cor_names = self.rm.cor_names
        bpm_names = self.rm.bpm_names
        inj_matrix = self.rm.matrix
        try:
            self.rm.load(self.rm_filename)
        except:
            print("No Response Matrix")
            return False
            
        if len(cor_names) > len(self.rm.cor_names) or len(bpm_names) > len(self.rm.bpm_names):
            print("dump calculated ORM")
            self.rm.cor_names = cor_names
            self.rm.bpm_names = bpm_names
            self.rm.matrix = inj_matrix
            self.rm.dump(filename=self.rm_filename)
        else:
            print("inject calculated ORM")
            self.rm.inject(cor_names, bpm_names, inj_matrix)

        if self.rm_filename != None:
            self.rm.dump(filename=self.rm_filename)

        if self.do_DRM_calc:
            if self.drm != None:
                self.drm.calculate(tw_init=self.tw_init)
            if self.drm_filename != None:
                self.rm.dump(filename=self.drm_filename)


class AutoCorrection(Thread):
    def __init__(self, orbit_class):
        super(AutoCorrection, self).__init__()
        self.orbit_class = orbit_class
        self._stop_event = Event()
        self.do = None
        self.delay = 1
        self.stop_event = False
    
    def one_correction(self):
        beam_on = self.orbit_class.read_orbit()
        time.sleep(0.01)
        if beam_on:
            self.orbit_class.correct()
            time.sleep(0.01)
            self.orbit_class.apply_kicks()
            time.sleep(0.5)
        else:
            print("no beam")
            time.sleep(1)
    
    def run(self):
        while not self.stop_event:
            self.one_correction()
            print("correct")
            time.sleep(self.delay)
            
    def stop(self):
        self._stop_event.set()


class OrbitInterface:
    """
    Main class for orbit correction
    """
    def __init__(self, parent):
        self.bpms4remove = ["BPMS.99.I1", "BPMS.192.B1"]
        self.corrs4remove = ["CBB.98.I1", "CBB.100.I1", "CBB.101.I1","CBB.191.B1", "CBB.193.B1", "CBB.202.B1",
            'CBL.73.I1', 'CBL.78.I1', 'CBL.83.I1', 'CBL.88.I1', 'CBL.90.I1', 'CBB.403.B2', 'CBB.405.B2', 'CBB.414.B2']
        self.parent = parent
        self.ui = parent.ui
        self.online_calc = True
        self.reset_undo_database()
        self.corrs = []
        self.hcors = []
        self.vcors = []
        self.s_bpm = []
        self.x_bpm = []
        self.y_bpm = []
        self.mi_orbit = MIOrbit()
        self.mi_orbit.mi = self.parent.mi
        self.calc_correction = {}
        self.p_init = None
        self.add_orbit_plot()
        self.ui.pb_check.clicked.connect(lambda: self.getRows(2, self.ui.table_cor))
        self.ui.pb_uncheck.clicked.connect(lambda: self.getRows(0, self.ui.table_cor))
        self.ui.pb_bpm_uncheck.clicked.connect(lambda: self.getRows(0, self.ui.table_bpm))
        self.ui.pb_bpm_check.clicked.connect(lambda: self.getRows(2, self.ui.table_bpm))
        #self.ui.pb_read_orbit.clicked.connect(self.read_orbit)
        self.ui.actionRead_BPMs_Corrs.triggered.connect(self.read_orbit)
        self.ui.pb_apply_kicks.clicked.connect(self.apply_kicks)

        #self.ui.pb_calc_RM.clicked.connect(self.calc_response_matrix)
        self.ui.actionCalculate_RM.triggered.connect(lambda: self.calc_response_matrix(do_DRM_calc=True))
        self.ui.actionCalculate_ORM.triggered.connect(lambda: self.calc_response_matrix(do_DRM_calc=False))
        #self.ui.pb_correct_orbit.clicked.connect(self.correct)
        self.ui.pb_correct_orbit.clicked.connect(self.read_and_correct)

        self.ui.pb_read_orbit.clicked.connect(self.read_bpms)
        self.ui.pb_calculate.clicked.connect(self.calculate_correction)

        self.ui.pb_reset_all.clicked.connect(self.undo)
        self.ui.cb_x_cors.stateChanged.connect(self.choose_plane)
        self.ui.cb_y_cors.stateChanged.connect(self.choose_plane)
        self.ui.pb_update_lat.clicked.connect(self.parent.read_quads)

        self.ui.pb_uncheck_red.clicked.connect(self.uncheck_red)

        self.ui.pb_online_orbit.clicked.connect(self.start_stop_live_orbit)


        #self.cavity = CavityA1(eid="CTRL.A1.I1")
        #self.cavity.mi = self.parent.mi
        self.ui.pb_feedback.clicked.connect(self.start_stop_feedback)

        self.rm_calc = pg.QtCore.QTimer()
        self.rm_calc.timeout.connect(self.is_rm_calc_alive)

        self.golden_orbit = GoldenOrbit(parent=self)
        self.ui.sb_apply_fraction.valueChanged.connect(self.set_values2correctors)
        #self.ui.cb_correction_result.stateChanged.connect(self.update_plot)

        

        self.ui.actionAdaptive_Feedback.triggered.connect(self.run_awindow)
        self.adaptive_feedback = None
        #self.adaptive_feedback = None
        #self.auto_correction = AutoCorrection(orbit_class=self)
        self.debug_mode = False
        if self.parent.mi.__class__ == TestMachineInterface:
            self.debug_mode = True
        
        self.ui.actionSave_corrs.triggered.connect(self.save_correctors)
        self.ui.actionLoad_corrs.triggered.connect(self.restore_correctors)

    def reset_undo_database(self):
        self.undo_data_base = []

    def run_awindow(self):
        if self.adaptive_feedback is None:
            self.adaptive_feedback = UIAFeedBack(orbit=self)
        self.adaptive_feedback.show()

    def uncheck_red(self):
        """
        Method to uncheck correctors if they are out of limits (red color in the GUI)

        :return:
        """
        corrs = self.get_dev_from_cb_state(self.corrs)

        for cor in corrs:
            if cor.ui.alarm:
                cor.ui.uncheck()
        bpms = self.get_dev_from_cb_state(self.bpms)

        for bpm in bpms:
            if bpm.ui.alarm:
                bpm.ui.uncheck()

    def choose_plane(self):
        """
        Method checks and unchecks corresponding correctors in horizontal or/and vertical planes

        :return:
        """
        x_plane = self.ui.cb_x_cors.isChecked()
        y_plane = self.ui.cb_y_cors.isChecked()

        if y_plane and not x_plane:
            for cor in self.corrs:
                if cor.__class__ == Hcor:
                    cor.ui.uncheck()
                    cor.ui.set_hide(True)
                else:
                    cor.ui.check()
                    cor.ui.set_hide(False)

        elif x_plane and not y_plane:
            for cor in self.corrs:
                if cor.__class__ == Hcor:
                    cor.ui.check()
                    cor.ui.set_hide(False)
                else:
                    cor.ui.uncheck()
                    cor.ui.set_hide(True)
        else:
            for cor in self.corrs:
                cor.ui.check()
                cor.ui.set_hide(False)


    def reset_all(self):
        """
        Method to reset initial values of the correctors

        :return:
        """
        corrs = self.get_dev_from_cb_state(self.corrs)
        self.online_calc = False
        for cor in corrs:
            kick_mrad = cor.ui.get_init_value()
            cor.ui.set_value(kick_mrad)
        self.online_calc = True

    def undo(self):
        """
        Method to reset initial values of the correctors

        :return:
        """
        if len(self.undo_data_base) == 0:
            return 0
        #cor_ids = [cor.id for cor in self.corrs]
        #corrs = self.get_dev_from_cb_state(self.corrs)
        self.online_calc = False
        corrs_dict = self.undo_data_base[-1]
        for cor in self.corrs:
            if cor.id in corrs_dict.keys():
                cor.ui.check()
                kick_mrad = corrs_dict[cor.id]
                #print(cor.id, kick_mrad)
                cor.ui.set_init_value(kick_mrad)
                cor.ui.set_value(kick_mrad)
            else:
                cor.ui.uncheck()
        del self.undo_data_base[-1]
        #print(len(self.undo_data_base))
        self.ui.pb_reset_all.setText("Undo (" + str(len(self.undo_data_base)) + ")")
        self.online_calc = True
        
        
        
    def save_correctors(self):
        corrs_save = {}
        for cor in self.corrs:
            kick_mrad = cor.ui.get_value()
            print(cor.id," save: ", cor.ui.get_init_value())
            corrs_save[cor.id] = cor.ui.get_init_value()
            
        with open("corrs_save.json", 'w') as f:
            json.dump(corrs_save, f)
            
            
    def restore_correctors(self):
        with open("corrs_save.json", 'r') as f:
            # data_new = pickle.load(f)
            table = json.load(f)        
        cor_ids = [cor.id for cor in self.corrs]
        self.online_calc = False
        for cor_id in table.keys():
            if cor_id in cor_ids:
                inx = cor_ids.index(cor_id)
                cor = self.corrs[inx]
                cor.ui.set_value(table[cor.id])
                print(cor.id," get: ", cor.ui.get_value(), table[cor.id])
        self.online_calc = True

    def apply_kicks(self):
        """
        Methos sends correctors kicks to DOOCS, if strengths below the limits,
        otherwise error box will appear

        :return:
        """

        corrs = self.get_dev_from_cb_state(self.corrs)

        for cor in corrs:
            if cor.ui.alarm:
                self.parent.error_box("kick exceeds limits. Try 'Uncheck Red' and recalculate correction")
                return 0

        for cor in corrs:
            kick_mrad = cor.ui.get_value()
            print(cor.id," set: ", cor.ui.get_init_value(), "-->", kick_mrad)
            cor.mi.set_value(kick_mrad)

        self.write_old_kicks(corrs)


    def write_old_kicks(self, corrs):
        old_corrs_kicks = {}
        save_flag = False
        for cor in corrs:
            # write to dict old kicker strengths
            old_corrs_kicks[cor.id] = cor.ui.get_init_value()
            if cor.ui.get_init_value() != cor.ui.get_value():
                save_flag = True
            #print(cor.id, old_corrs_kicks[cor.id])
        if save_flag:
            self.undo_data_base.append(old_corrs_kicks)
            self.ui.pb_reset_all.setText("Undo (" + str(len(self.undo_data_base)) + ")")

    #def read_all_bpms(self):
    #    bpm_server = "ORBIT"
    #    orbit_x = self.parent.mi.get_value("XFEL.DIAG/" + bpm_server + "/*/X.SA1")
    #    orbit_y = self.parent.mi.get_value("XFEL.DIAG/" + bpm_server + "/*/Y.SA1")
    #    names = np.array([data["str"] for data in orbit_x["data"]])
    #    values_x = np.array([data["float"] for data in orbit_x["data"]])
    #    values_y = np.array([data["float"] for data in orbit_y["data"]])




    #def read_bpms(self, n_readings, n_last_readings):
    #    """
    #    Method to read from MI BPMs (X and Y: mm -> m) and checks charge on the BPMs
    #    if the charge below charge_thresh return False
    #
    #    :param n_readings:
    #    :param n_last_readings:
    #    :return:
    #    """
    #
    #    if n_last_readings> n_readings:
    #        print("wrong settings")
    #        return
    #
    #    charge_thresh = 0.005
    #    bpms = self.get_dev_from_cb_state(self.bpms)
    #    beam_on = True
    #    for i in range(n_readings):
    #
    #        for elem in bpms:
    #            if "x_array" not in elem.__dict__:
    #                elem.x_array = []
    #            if "y_array" not in elem.__dict__:
    #                elem.y_array = []
    #
    #            try:
    #
    #                charge = elem.mi.get_charge()
    #                if charge < charge_thresh:
    #                    beam_on = False
    #                    continue
    #
    #                x_mm, y_mm = elem.mi.get_pos()
    #
    #                if np.isnan(x_mm) or np.isnan(y_mm):
    #                    print("BPM: " + elem.id + " was unchecked NAN")
    #                    #elem.ui.uncheck()
    #                    continue
    #                elem.x_array.append(x_mm/1000.)
    #                elem.y_array.append(y_mm/1000.)
    #            except:
    #                print("BPM: " + elem.id + " error reading")
    #        time.sleep(0.1)
    #
    #    for elem in bpms:
    #        if "x_array" not in elem.__dict__ or "y_array" not in elem.__dict__ :
    #            elem.ui.uncheck()
    #            print("no data")
    #            continue
    #        elif len(elem.x_array) == 0 or len(elem.y_array) == 0:
    #            elem.ui.uncheck()
    #            print("no data")
    #            continue
    #        else:
    #            elem.x = np.mean(np.array(elem.x_array)[-n_last_readings:])   # in [m]
    #            elem.y = np.mean(np.array(elem.y_array)[-n_last_readings:])   # in [m]
    #            elem.ui.set_value((elem.x*1000., elem.y*1000))                # table in [mm]
    #
    #    return beam_on

    def read_correctors(self):
        """
        Method to read from MI correctors (angles: mrad->rad)
        self.online_calc = False - switch off recalculating of the calculated orbit
        otherwise after every set in table orbit will be recalculated.

        :return:
        """
        self.online_calc = False

        for elem in self.corrs:
            elem.kick_mrad = elem.mi.get_value()
            elem.angle_read = elem.kick_mrad*1e-3
            elem.i_kick = elem.kick_mrad
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)

        self.online_calc = True
        self.parent.lat.update_transfer_maps()



    def read_orbit(self):
        """
        Method to readw from MI: correctors (angles: mrad->rad) and
        BPMs (X and Y: mm -> m) and checks charge on the BPMs
        if the charge below charge_thresh return False

        :return: bool, True if the charge on all BPMs >= charge_thresh otherwise False
        """

        #self.online_calc = False
        #
        #for elem in self.corrs:
        #    elem.kick_mrad = elem.mi.get_value()
        #    elem.angle_read = elem.kick_mrad*1e-3
        #    elem.i_kick = elem.kick_mrad
        #    elem.ui.set_init_value(elem.kick_mrad)
        #    elem.ui.set_value(elem.kick_mrad)
        #
        #self.online_calc = True
        #self.parent.lat.update_transfer_maps()
        self.read_correctors()

        charge_thresh = 0.005



        bpms = self.get_dev_from_cb_state(self.bpms)

        beam_on = True
        for elem in bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                if np.isnan(x_mm) or np.isnan(y_mm):
                    print("BPM: " + elem.id + " was unchecked NAN")
                    elem.ui.uncheck()
                charge = elem.mi.get_charge()
                if charge < charge_thresh:
                    beam_on = False
                elem.x = x_mm/1000.
                elem.y = y_mm/1000.
                elem.ui.set_value((x_mm, y_mm))
            except:
                print("BPM: " + elem.id + " was unchecked ")
                elem.ui.uncheck()
        #beam_on = self.read_bpms(n_readings=1, n_last_readings=1)
        #self.update_cors_plot()
        self.update_plot()
        return beam_on



    #def update_cors_plot(self):
    #    """
    #    Method to update corrector bars on the plot.
    #    High of the bars depends on the corrector amplitude
    #
    #    :return:
    #    """
    #
    #    kicks = [elem.kick_mrad for elem in self.corrs]
    #    self.plot_cor.setYRange(np.floor(min(kicks)), np.ceil(max(kicks)))
    #
    #    for elem in self.corrs:
    #        if np.abs(np.abs(elem.kick_mrad) - np.abs(elem.i_kick))> 0.001:
    #            self.r_items[elem.ui.row].setBrush(pg.mkBrush("r"))
    #            self.ui.table_cor.item(elem.row, 1).setForeground(QtGui.QColor(255, 101, 101))  # red
    #        else:
    #            self.ui.table_cor.item(elem.row, 1).setForeground(QtGui.QColor(255, 255, 255))  # white
    #            self.r_items[elem.ui.row].setBrush(pg.mkBrush("g"))
    #        r = self.r_items[elem.ui.row]
    #        sizes = r.init_params
    #        sizes[3] = elem.kick_mrad/self.cor_ampl
    #        r.setRect(sizes[0]-0.1, sizes[1], sizes[2]+0.1, sizes[3])

    def calc_orbit(self):
        """
        function calculates the orbit taking into account correctors strength

        :return: None
        """

        if self.online_calc == False:
            return

        for elem in self.parent.lat.sequence:
            if elem.__class__ in [Hcor, Vcor]:
                elem.kick_mrad = elem.ui.get_value()
                kick_mrad_i = elem.ui.get_init_value()
                warn = (np.abs(elem.kick_mrad) - np.abs(elem.ui.get_init_value())) > 0.5
                elem.ui.check_values(elem.kick_mrad, elem.lims, warn=warn)
                angle = (elem.kick_mrad - kick_mrad_i)/1000.
                elem.angle = angle
                elem.transfer_map = self.parent.lat.method.create_tm(elem)
        #self.update_cors_plot()
        self.update_plot()

    def create_Orbit_obj(self):
        """
        function creates the Orbit object with correctors and bpms which are active in the GUI
        NewOrbit - is object form ocelot.cpbd.orbitcorrection

        :return: Orbit
        """
        #for elem in self.corrs:
        #    print("angle = ", elem.angle)
        self.orbit = NewOrbit(self.parent.lat, empty=True, rm_method=LinacRmatrixRM,
                              disp_rm_method=LinacDisperseSimRM)
        corrs = self.get_dev_from_cb_state(self.corrs)
        if len(corrs) == 0:
            self.parent.error_box("No correctors for correction")
            return None
        s_pos = np.min([cor.s for cor in corrs])
        bpms = np.array(self.bpms)
        bpms_unch = bpms[np.array([bpm.s for bpm in self.bpms]) < s_pos]
        [bpm.ui.uncheck() for bpm in bpms_unch]
        bpms = self.get_dev_from_cb_state(bpms)
        if len(bpms) == 0:
            self.parent.error_box("No BPM")
            return None
        self.orbit.bpms = bpms
        self.orbit.corrs = corrs
        self.hcors = []
        self.vcors = []
        for cor in corrs:
            if cor.__class__ == Hcor:
                self.hcors.append(cor)
            else:
                self.vcors.append(cor)

        self.orbit.hcors = self.hcors
        self.orbit.vcors = self.vcors

        self.orbit.setup_response_matrix()
        self.orbit.setup_disp_response_matrix()

        return self.orbit


    def load_response_matrices(self):
        """
        Method to load ORM and DRM from the file.

        :return: True if the corresponding file exists and False if not
        """

        print(self.parent.rm_files_dir + "RM_" + self.ui.cb_lattice.currentText() + ".json")
        try:
            self.orbit.response_matrix.load(self.parent.rm_files_dir + "RM_" + self.ui.cb_lattice.currentText() + ".json")
        except:
            print("No Response Matrix")
            return False
        try:
            self.orbit.disp_response_matrix.load(self.parent.rm_files_dir + "DRM_" + self.ui.cb_lattice.currentText() + ".json")
        except:
            print("No Dispersion Response Matrix")
            return True

        return True

    def is_rm_ok(self, orbit):
        """
        Method to check and load if needed the RMs

        :return: True -  if shape of the ORM (!) is correct (shape of the DRM is not checked)
                 False - if the RM does not exist or RM load was failed
        """
        if len(self.orbit.response_matrix.matrix) == 0:
            print("tring to load response matrix ... Is OK?")
            is_ok = self.load_response_matrices()
            print(is_ok)
            if not is_ok:
                return is_ok
        cor_list = [cor.id for cor in np.append(orbit.hcors, orbit.vcors)]
        bpm_list = [bpm.id for bpm in orbit.bpms]
        RM = self.orbit.response_matrix.extract(cor_list=cor_list, bpm_list=bpm_list)
        if np.shape(RM)[0] != len(bpm_list)*2 or np.shape(RM)[1] != len(cor_list):
            return False
        else:
            return True

    def close_orbit(self):
        """
        Method sets BPM.x_ref and BPM.y_ref from dictionary: self.golden_orbit

        :return:
        """
        n_bpms = len(self.orbit.bpms)
        if n_bpms < 10:
            self.ui.cb_close_orbit.setChecked(False)

        for i, elem in enumerate(self.orbit.bpms[-5:]):

            elem.x_ref = elem.x
            elem.y_ref = elem.y
            print(elem.id, "set close orbit")

    def set_values2correctors(self):

        apply_fraction = self.ui.sb_apply_fraction.value()
        self.online_calc = False
        for cor in self.corrs:
            kick_mrad_old = cor.ui.get_init_value()
            if cor.id in self.calc_correction.keys():
                cor.angle = self.calc_correction[cor.id]

            delta_kick_mrad = cor.angle*1000*apply_fraction
            #print(cor.angle*1000, delta_kick_mrad)
            new_kick_mrad = kick_mrad_old + delta_kick_mrad
            cor.kick_mrad =  new_kick_mrad
            cor.ui.set_value(cor.kick_mrad)
            
            if np.abs(delta_kick_mrad)> 0.001:
                self.ui.table_cor.item(cor.row, 1).setForeground(QtGui.QColor(255, 101, 101))  # red
            else:
                self.ui.table_cor.item(cor.row, 1).setForeground(QtGui.QColor(255, 255, 255))  # white
                
            warn = (np.abs(new_kick_mrad) - np.abs(kick_mrad_old)) > 0.5

            cor.ui.check_values(cor.kick_mrad, cor.lims, warn)
        self.online_calc = True
        self.calc_orbit()

    def read_bpms(self):
        self.parent.mi.set_value("XFEL.UTIL/BUNCH_PATTERN/SA1/NUM_BUNCHES_REQUESTED", 1)
        self.parent.mi.set_value("XFEL.UTIL/BUNCH_PATTERN/SA1/BEAM_ALLOWED", 1)
        
        self.read_correctors()
        self.mi_orbit.read_and_average(nreadings=self.parent.gc_nreadings, take_last_n=self.parent.gc_nlast)
        self.parent.mi.set_value("XFEL.UTIL/BUNCH_PATTERN/SA1/BEAM_ALLOWED", 0)
        self.calculate_correction()

    def calculate_correction(self):

        bpms = self.get_dev_from_cb_state(self.bpms)
        checked_bpms_id = [bpm.id for bpm in bpms]
        self.mi_orbit.get_bpms(bpms)
        bpms = self.get_dev_from_cb_state(self.bpms)
        charge_thresh = 0.005

        for elem in bpms:

            if np.isnan(elem.x) or np.isnan(elem.y):
                print("BPM: " + elem.id + " was unchecked NAN")
                elem.ui.uncheck()
            if elem.charge < charge_thresh:
                elem.ui.uncheck()
            elem.ui.set_value((elem.x*1000, elem.y*1000))

        self.update_plot()
        
        self.uncheck_red()
        
        self.correct()

        for elem in bpms:
            if elem.id in checked_bpms_id:
                elem.ui.check()


    def read_and_correct(self):
        self.read_orbit()

        self.uncheck_red()

        self.correct()


    def correct(self):
        """
        Method to the Orbit correction. Method calculate correctors strengths (kicks)
        and call function to calculate (self.calc_orbit()) and draw orbit on the plot
        but does not send it to the DOOCS server.

        :return:
        """

        #self.read_correctors()


        #self.read_orbit()

        #self.uncheck_red()

        self.orbit = self.create_Orbit_obj()
        if self.orbit == None:
            return 
        if not self.is_rm_ok(self.orbit):
            self.parent.error_box("Calculate Response Matrix")
            return 0

        self.golden_orbit.dict2golden_orbit()

        if self.ui.cb_close_orbit.isChecked():
            self.close_orbit()

        self.calc_correction = {}
        for cor in self.corrs:
            cor.angle = 0.
            self.calc_correction[cor.id] = cor.angle
        
        alpha = self.ui.sb_alpha.value()
        self.orbit.correction(alpha=alpha, p_init=None, epsilon_x=1e-3, epsilon_y=1e-3)

        for cor in self.corrs:
            self.calc_correction[cor.id] = cor.angle

        self.set_values2correctors()


    def start_stop_feedback(self):
        """
        Method to start/stop feedback timer.
        sb_feedback_sec - spinBox - set seconds for timer
        pb_feedback - pushBatton Off/On
        feedback_timer - timer
        :return:
        """
        delay = self.ui.sb_feedback_sec.value()*1000
        if self.ui.pb_feedback.text() == "Orbit Keeper Off":
            self.parent.feedback_timer.stop()
            self.ui.pb_feedback.setStyleSheet("color: rgb(85, 255, 127);")
            self.ui.pb_feedback.setText("Orbit Keeper On")
        else:

            self.parent.feedback_timer.start(delay)
            self.ui.pb_feedback.setText("Orbit Keeper Off")
            self.ui.pb_feedback.setStyleSheet("color: red")

    def start_stop_feedback_new(self):
        """
        Method to start/stop feedback timer.
        sb_feedback_sec - spinBox - set seconds for timer
        pb_feedback - pushBatton Off/On
        feedback_timer - timer
        :return:
        """
        delay = self.ui.sb_feedback_sec.value()
        if self.ui.pb_feedback.text() == "Orbit Keeper Off":
            self.auto_correction.stop_event = True
            self.auto_correction.stop()
            self.ui.pb_feedback.setStyleSheet("color: rgb(85, 255, 127);")
            self.ui.pb_feedback.setText("Orbit Keeper On")
        else:
            self.auto_correction = AutoCorrection(orbit_class=self)
            self.auto_correction.delay = delay
            self.auto_correction.stop_event = False
            self.auto_correction.start()
            self.ui.pb_feedback.setText("Orbit Keeper Off")
            self.ui.pb_feedback.setStyleSheet("color: red")


    def auto_correction(self):
        """
        Method repeats correction in a loop.
        repetation rate is defined by spinBox - sb_feedback_sec
        feedback_timer - QTimer to repats correction oin different thread

        :return:
        """
        beam_on = self.read_orbit()
        time.sleep(0.01)
        if beam_on:
            self.correct()
            time.sleep(0.01)
            self.apply_kicks()
            time.sleep(0.5)
        else:
            print("no beam")
            time.sleep(1)

    def get_dev_from_cb_state(self, devs):

        """
        Gets list of all pvs that have checked boxes.

        Returns:
                List of PV strings
        """
        checked_devs = []
        for dev in devs:
            state = dev.ui.state()
            #print(dev.id, state)
            if state == 2:
                checked_devs.append(dev)
        return checked_devs


    def calc_response_matrix(self, do_DRM_calc=True):
        """
        Method is connected to pushBatton pb_calc_RM and creates ResponseMatrixCalculator
        which calculates ORM and DRM in different thread
        self.parent.rm_files_dir - name of directory for RMs sore
        self.ui.cb_lattice.currentText() - name of the sections (e.g. "I1D, L1, SASE1 and so on)

        The method also launchs the Qtimer self.rm_calc to controle when the thread
        ResponseMatrixCalculator finishs the calculations

        :return:
        """

        self.orbit = self.create_Orbit_obj()
        if self.orbit == None:
            return
        self.RMs = ResponseMatrixCalculator(rm=self.orbit.response_matrix,
                                      drm=self.orbit.disp_response_matrix)
        self.RMs.do_DRM_calc = do_DRM_calc

        self.ui.pb_correct_orbit.setText("RMs are calculated. Please Wait...")
        self.ui.pb_correct_orbit.setStyleSheet("color: red")

        self.RMs.tw_init = self.parent.tws0
        self.RMs.rm_filename = self.parent.rm_files_dir + "RM_" + self.ui.cb_lattice.currentText() + ".json"
        self.RMs.drm_filename = self.parent.rm_files_dir + "DRM_" + self.ui.cb_lattice.currentText() + ".json"
        self.RMs.start()
        self.rm_calc.start()


    def is_rm_calc_alive(self):
        """
        Method to check if the ResponseMatrixCalculator thread is alive.
        it is needed to change name and color of the pushBatton pb_calc_RM.
        When RMs caclulation is finished. If the thread is dead QTimer self.rm_calc is stopped

        :return:
        """
        if not self.RMs.is_alive():
            self.ui.pb_correct_orbit.setStyleSheet("color: rgb(85, 255, 127);")
            self.ui.pb_correct_orbit.setText("Calculate Correction")
            self.rm_calc.stop()


    def load_correctors(self):
        """

        """
        self.corrs = self.load_devices(types=[Hcor, Vcor])

        self.parent.add_devs2table(self.corrs, w_table=self.ui.table_cor, calc_obj=self.calc_orbit,
                                   spin_params=[-100, 100, 0.1], check_box=True)
        self.cor_ampl = np.max(np.append(1, np.abs(np.array([q.kick_mrad for q in self.corrs]))))
        self.ui.table_cor.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


    def load_bpms(self, lat):
        devices = []
        L = 0
        for i, elem in enumerate(lat.sequence):
            L += elem.l
            if elem.__class__ in [Monitor]:
                elem.s = L - elem.l/2.
                devices.append(elem)

                mi_dev = BPM(eid=elem.id)
                mi_dev.mi = self.parent.mi
                elem.mi = mi_dev
                elem.lat_inx = i
                elem.x = 0
                elem.y = 0
                elem.Dx = 0
                elem.Dy = 0
                elem.Dx_des = 0
                elem.Dy_des = 0
                elem.weight = 1

        return devices

    def add_bpms2table(self, devs, w_table, check_box=False):
        """ Initialize the UI table object """

        self.spin_boxes = []
        w_table.setRowCount(0)
        for row in range(len(devs)):
            #eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            w_table.setRowCount(row + 1)
            pv = devs[row].id
            # put PV in the table
            w_table.setItem(row, 0, QtGui.QTableWidgetItem(str(pv)))
            # put start val in
            w_table.setItem(row, 1, QtGui.QTableWidgetItem(str(devs[row].x)))
            w_table.setItem(row, 2, QtGui.QTableWidgetItem(str(devs[row].y)))

            w_table.resizeColumnsToContents()
            #header = w_table.horizontalHeader()
            #header.setStretchLastSection(True)
            #header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)

            if check_box:
                checkBoxItem = QtGui.QTableWidgetItem()
                # checkBoxItem.setBackgroundColor(QtGui.QColor(100,100,150))
                checkBoxItem.setCheckState(QtCore.Qt.Checked)
                flags = checkBoxItem.flags()
                checkBoxItem.setFlags(flags)
                w_table.setItem(row, 3, checkBoxItem)
                #checkBoxItem.itemChanged.connect(self.calc_orbit)

            devs[row].row = row

            ui = BPMUI()
            ui.tableWidget = w_table
            ui.row = row
            ui.col = 2
            devs[row].ui = ui

    def uncheck_bpms(self, bpms, bmps4uncheck):
        for bpm in bpms:
            if bpm.id in bmps4uncheck:
                bpm.ui.uncheck()

    def uncheck_corrs(self, corrs, cors4uncheck):
        for cor in corrs:
            if cor.id in cors4uncheck:
                cor.ui.uncheck()

    def load_orbit_devs(self):

        self.bpms = self.load_bpms(lat=self.parent.lat)
        self.add_bpms2table(self.bpms, w_table=self.ui.table_bpm, check_box=True)
        self.uncheck_bpms(self.bpms, self.bpms4remove)
        self.load_correctors()

        self.uncheck_corrs(self.corrs, self.corrs4remove)


        #self.r_items = self.parent.plot_lat(plot_wdg=self.plot_cor, types=[Hcor, Vcor], x_scale=2)


    def load_devices(self, types, load_all=False):
        devices = []
        mi_devs = {}
        lat_seq = self.parent.lat.sequence
        if load_all:
            lat_seq = self.parent.big_sequence
        L = 0
        for i, elem in enumerate(lat_seq):
            L += elem.l
            if elem.__class__ in types:
                elem.s = L - elem.l / 2.
                elem.kick_mrad = elem.angle* 1000.
                elem.i_kick = elem.kick_mrad

                elem.lat_inx = i

                if "ps_id" in elem.__dict__:
                    if elem.ps_id not in mi_devs.keys():
                        mi_dev = Corrector(eid=elem.id)
                        mi_dev.mi = self.parent.mi
                        elem.mi = mi_dev
                        mi_devs[elem.ps_id] = mi_dev
                    else:
                        elem.mi = mi_devs[elem.ps_id]
                else:
                    mi_dev = Corrector(eid=elem.id)
                    mi_dev.mi = self.parent.mi
                    elem.mi = mi_dev

                elem.lims = elem.mi.get_limits()
                if self.debug_mode:
                    elem.lims = [-1, 1]
                if elem.__class__ == Hcor:
                    self.hcors.append(elem)
                elif elem.__class__ == Vcor:
                    self.vcors.append(elem)
                else:
                    print("wrong type")
                devices.append(elem)

        return devices


    def add_orbit_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_x = win.addPlot(row=0, col=0)

        #win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot_x.showGrid(1, 1, 1)
        self.plot_y = win.addPlot(row=1, col=0)
        self.plot_x.setXLink(self.plot_y)

        self.plot_y.showGrid(1, 1, 1)

        self.plot_y.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.w_orbit.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()


        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Y calc', antialias=True)
        self.plot_y.addItem(self.orb_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4)
        self.orb_y_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y', antialias=True)
        self.plot_y.addItem(self.orb_y_ref)

        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=3)
        self.orb_y_golden = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y golden', antialias=True)

        color = QtGui.QColor(0, 255, 0)
        pen = pg.mkPen(color, width=2)
        self.orb_y_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y live', antialias=True)

        #self.plot_cor = win.addPlot(row=2, col=0)
        #win.ci.layout.setRowMaximumHeight(2, 150)

        #self.plot_cor.setXLink(self.plot_y)
        #self.plot_cor.showGrid(1, 1, 1)

        #self.plot_cor.addItem(pg.InfiniteLine(pos =62.09,  angle=90, movable=False), ignoreBounds=True)
        #lh_t = pg.TextItem("I1", anchor=(0, 0))
        #lh_t.setPos(62.09, 0)
        #self.plot_cor.addItem(lh_t, ignoreBounds=True)

        #i1_pos = 62.09
        #dl_pos = 23.2 + 72
        #bc0_pos = 79 + 23.2
        #l1_pos = 150 + 23.2
        #bc1_pos = 180 + 23.2
        #l2_pos = 360 + 23.2
        #bc2_pos = 392 + 23.2
        #l3_pos = 1435 + 23.2
        #cl_pos = 1830 + 23.2
        #self.plot_cor.addItem(pg.InfiniteLine(pos =i1_pos,  angle=90, movable=False), ignoreBounds=True)
        #lh_t = pg.TextItem("I1", anchor=(0, 0))
        #lh_t.setPos(i1_pos, 0)
        #self.plot_cor.addItem(lh_t, ignoreBounds=True)


        #self.plot_cor.addItem(pg.InfiniteLine(pos =bc0_pos,  angle=90, movable=False), ignoreBounds=True)
        #bc0_t = pg.TextItem("BC0", anchor=(0, 0))
        #bc0_t.setPos(bc0_pos, 0)
        #self.plot_cor.addItem(bc0_t, ignoreBounds=True)
        #
        #self.plot_cor.addItem(pg.InfiniteLine(pos =l1_pos,  angle=90, movable=False), ignoreBounds=True)
        #l1_t = pg.TextItem("L1", anchor=(0, 0))
        #l1_t.setPos(l1_pos, 0)
        #self.plot_cor.addItem(l1_t, ignoreBounds=True)
        #
        #self.plot_cor.addItem(pg.InfiniteLine(pos =bc1_pos,  angle=90, movable=False), ignoreBounds=True)
        #bc1_t = pg.TextItem("BC1", anchor=(0, 0))
        #bc1_t.setPos(bc1_pos, 0)
        #self.plot_cor.addItem(bc1_t, ignoreBounds=True)
        #
        #self.plot_cor.addItem(pg.InfiniteLine(pos =l2_pos,  angle=90, movable=False), ignoreBounds=True)
        #l2_t = pg.TextItem("L2", anchor=(0, 0))
        #l2_t.setPos(l2_pos, 0)
        #self.plot_cor.addItem(l2_t, ignoreBounds=True)
        #
        #self.plot_cor.addItem(pg.InfiniteLine(pos =bc2_pos,  angle=90, movable=False), ignoreBounds=True)
        #bc2_t = pg.TextItem("BC2", anchor=(0, 0))
        #bc2_t.setPos(bc2_pos, 0)
        #self.plot_cor.addItem(bc2_t, ignoreBounds=True)
        #
        #self.plot_cor.addItem(pg.InfiniteLine(pos =l3_pos,  angle=90, movable=False), ignoreBounds=True)
        #l3_t = pg.TextItem("L3", anchor=(0, 0))
        #l3_t.setPos(l3_pos, 0)
        #self.plot_cor.addItem(l3_t, ignoreBounds=True)
        #
        #self.plot_cor.addItem(pg.InfiniteLine(pos =cl_pos,  angle=90, movable=False), ignoreBounds=True)
        #cl_t = pg.TextItem("CL", anchor=(0, 0))
        #cl_t.setPos(cl_pos, 0)
        #self.plot_cor.addItem(cl_t, ignoreBounds=True)

        self.plot_x.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen,  name='X calc', antialias=True)

        self.plot_x.addItem(self.orb_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4, symbolPen='o')
        self.orb_x_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X', antialias=True)
        self.plot_x.addItem(self.orb_x_ref)

        color = QtGui.QColor(0, 255, 0)
        pen = pg.mkPen(color, width=2)
        self.orb_x_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X live', antialias=True)

        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=2)
        self.orb_x_golden= pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X golden', antialias=True)

        #self.plot_cor.sigRangeChanged.connect(self.zoom_signal)
        #self.plot_cor.setYRange(-3, 3)
        self.plot_x.sigRangeChanged.connect(self.zoom_signal)
        self.plot_x.setYRange(-2, 2)
        self.plot_y.setYRange(-2, 2)

    def zoom_signal(self):
        if len(self.corrs) == 0:
            return

        s_up = self.plot_y.viewRange()[0][0]
        s_down = self.plot_y.viewRange()[0][1]


        s_pos = np.array([q.s for q in self.corrs]) + self.parent.lat_zi
        s_up = s_up if s_up <= s_pos[-1] else s_pos[-1]
        s_down = s_down if s_down >= s_pos[0] else s_pos[0]

        s_bpm_pos = np.array([q.s for q in self.bpms]) + self.parent.lat_zi
        s_bpm_up = s_up if s_up <= s_bpm_pos[-1] else s_bpm_pos[-1]
        s_bpm_down = s_down if s_down >= s_bpm_pos[0] else s_bpm_pos[0]

        indexes = np.arange(np.argwhere(s_pos >= s_up)[0][0], np.argwhere(s_pos <= s_down)[-1][0] + 1)
        mask = np.ones(len(self.corrs), np.bool)
        mask[indexes] = 0
        self.corrs = np.array(self.corrs)
        [q.ui.set_hide(hide=False) for q in self.corrs[indexes]]
        [q.ui.set_hide(hide=True) for q in self.corrs[mask]]

        #[q.ui.check() for q in self.corrs[indexes]]
        #[q.ui.uncheck() for q in self.corrs[mask]]
        s_bpm_pos = np.array([q.s for q in self.bpms]) + self.parent.lat_zi
        s_bpm_up = s_bpm_up if s_bpm_up <= s_bpm_pos[-1] else s_bpm_pos[-1]
        s_bpm_down = s_bpm_down if s_bpm_down >= s_bpm_pos[0] else s_bpm_pos[0]

        indexes_bpm = np.arange(np.argwhere(s_bpm_pos >= s_bpm_up)[0][0], np.argwhere(s_bpm_pos <= s_bpm_down)[-1][0] + 1)
        mask_bpm = np.ones(len(self.bpms), np.bool)
        mask_bpm[indexes_bpm] = 0
        self.bpms = np.array(self.bpms)
        [q.ui.set_hide(hide=False) for q in self.bpms[indexes_bpm]]
        [q.ui.set_hide(hide=True) for q in self.bpms[mask_bpm]]



    def start_stop_live_orbit(self):
        if self.ui.pb_online_orbit.text() == "Live Orbit Off":
            self.parent.timer_live.stop()
            self.ui.pb_online_orbit.setStyleSheet("color: rgb(85, 255, 255);")
            self.ui.pb_online_orbit.setText("Live Orbit On")

            self.plot_x.removeItem(self.orb_x_live)
            self.plot_y.removeItem(self.orb_y_live)
            self.plot_x.legend.removeItem(self.orb_x_live.name())
            self.plot_y.legend.removeItem(self.orb_y_live.name())

        else:
            self.parent.timer_live.start(1000)
            self.ui.pb_online_orbit.setText("Live Orbit Off")
            self.ui.pb_online_orbit.setStyleSheet("color: rgb(85, 255, 127);")
            self.plot_x.addItem(self.orb_x_live)
            self.plot_y.addItem(self.orb_y_live)


    def live_orbit(self):

        s_bpm = np.array([])
        x_bpm = np.array([])
        y_bpm = np.array([])
        bpms = self.get_dev_from_cb_state(self.bpms)
        for elem in bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                s_bpm = np.append(s_bpm, elem.s)
                x_bpm = np.append(x_bpm, x_mm - elem.x_ref*1000)
                y_bpm = np.append(y_bpm, y_mm - elem.y_ref*1000)
            except:
                print("could not read BPM", elem.id)

        s_bpm += self.parent.lat_zi

        #print("LIVE")
        self.orb_x_live.setData(x=s_bpm, y=x_bpm)
        self.orb_y_live.setData(x=s_bpm, y=y_bpm)
        self.orb_y.update()
        self.orb_x.update()

    def update_plot(self):

        #start = time.time()
        p_list = lattice_track(self.parent.lat, Particle(E=self.parent.tws0.E))
        #print("3 = ", start - time.time())

        x = np.array([p.x for p in p_list])*1000
        y = np.array([p.y for p in p_list])*1000
        s = np.array([p.s for p in p_list]) + self.parent.lat_zi

        bpms = self.get_dev_from_cb_state(self.bpms)

        s_bpm = np.array([bpm.s for bpm in bpms]) + self.parent.lat_zi

        x_bpm = np.array([bpm.x - bpm.x_ref for bpm in bpms])*1000
        y_bpm = np.array([bpm.y - bpm.y_ref for bpm in bpms])*1000

        indx = np.searchsorted(s, s_bpm)
        x_bpms_track = x[indx]
        y_bpms_track = y[indx]
        # Line
        self.orb_x_ref.setData(x=s_bpm, y=x_bpm)
        self.orb_y_ref.setData(x=s_bpm, y=y_bpm)

        if self.parent.show_correction_result: #otherwise "changes"
            self.orb_x.setData(x=s_bpm, y=x_bpm + x_bpms_track)
            self.orb_y.setData(x=s_bpm, y=y_bpm + y_bpms_track)
        else:
            self.orb_x.setData(x=s, y=x)
            self.orb_y.setData(x=s, y=y)



        #self.orb_y.setData(x=s, y=y)

        #self.plot_cor.update()
        self.orb_y.update()
        self.orb_x.update()

    def uncheckBoxes(self):
        """ Method to unchecked all active boxes """
        for cor in self.corrs:
            cor.ui.uncheck()


    def getRows(self, state, widget):
        """
        Method to set the UI checkbox state from slected rows.

        Loops though the rows and gets the selected state from the 'Active" column.
        If highlighted, check box is set the the 'state' input arg.

        Args:
                state (bool): Bool of whether the boxes should be checked or unchecked.
        """
        rows=[]
        for idx in widget.selectedIndexes():
            rows.append(idx.row())
            item = widget.item(idx.row(), 3)
            if item.flags() == QtCore.Qt.NoItemFlags:
                print("item disabled")
                continue
            item.setCheckState(state)


