"""
Sergey Tomin, XFEL/DESY, 2017
"""
import numpy as np
from mint.devices import *
import time
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore


class DispersionInterface:
    def __init__(self, parent):
        self.ui = parent.ui
        self.parent = parent
        self.ui.pb_start_meas.clicked.connect(self.dispersion_measurement)
        self.add_orbit_plot()
        self.ui.cb_cav_list.addItem("A1.I1")
        self.ui.cb_cav_list.addItem("A2.L1")
        self.ui.cb_cav_list.addItem("A3.L2")
        self.ui.cb_cav_list.addItem("A4.L2")
        self.ui.cb_cav_list.addItem("A5.L2")

        self.ui.cb_cav_list.addItem("A6.L3")
        self.ui.cb_cav_list.addItem("A7.L3")
        self.ui.cb_cav_list.addItem("A8.L3")
        self.ui.cb_cav_list.addItem("A9.L3")
        self.ui.cb_cav_list.addItem("A10.L3")
        self.ui.cb_cav_list.addItem("A11.L3")
        self.ui.cb_cav_list.addItem("A12.L3")
        self.ui.cb_cav_list.addItem("A13.L3")
        self.ui.cb_cav_list.addItem("A14.L3")
        self.ui.cb_cav_list.addItem("A15.L3")
        self.ui.cb_cav_list.addItem("A16.L3")
        self.ui.cb_cav_list.addItem("A17.L3")
        self.ui.cb_cav_list.addItem("A18.L3")
        self.ui.cb_cav_list.addItem("A19.L3")
        self.ui.cb_cav_list.addItem("A20.L3")
        self.ui.cb_cav_list.addItem("A21.L3")
        self.ui.cb_cav_list.addItem("A22.L3")
        self.ui.cb_cav_list.addItem("A23.L3")
        self.ui.cb_cav_list.addItem("A24.L3")
        self.ui.cb_cav_list.addItem("A25.L3")

        self.multilines_x = {}
        self.multilines_y = {}

    def read_bpms(self, bpms):
        """
        Method to read bpms

        :param bpms: list of the bpm objects
        :return: X, Y, bpm_list - List of the X and Y beam positions in [m] and list of the bpm names
        """
        x = []
        y = []
        bpm_list = []
        for bpm in bpms:
            x_mm, y_mm = bpm.mi.get_pos()
            charge = bpm.mi.get_charge()
            bpm_list.append(bpm.id)
            x.append(x_mm * 0.001)
            y.append(y_mm * 0.001)
        return np.array(x), np.array(y), bpm_list

    def get_orbit(self, bpms):
        n_readings = int(self.ui.sb_n_readings.value())
        n_bpms = len(bpms)
        X = np.zeros(n_bpms)
        Y = np.zeros(n_bpms)
        for n in range(n_readings):
            x, y, bpm_list = self.read_bpms(bpms)
            X = np.vstack((X, x))
            Y = np.vstack((Y, y))
            time.sleep(0.11)
        s_bpm = np.array([bpm.s for bpm in bpms])
        x_mean = np.mean(X, axis=0)
        y_mean = np.mean(Y, axis=0)
        x_std = np.std(x, axis=0)
        y_std = np.std(y, axis=0)
        return x_mean, y_mean, x_std, y_std

    def get_section_energy(self):

        current_lat = self.ui.cb_lattice.currentText()
        if current_lat in ["CL", "SASE1", "T4", "SASE3"]:
            energy = self.parent.mi.get_value(self.parent.le_cl_energy)
            #energy = self.parent.mi.get_value("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/CL/ENERGY.SA1")
        elif current_lat in ["B2"]:
            energy = self.parent.mi.get_value(self.parent.le_b2_energy)
        elif current_lat in ["B1"]:
            energy = self.parent.mi.get_value(self.parent.le_b1_energy)
        else:
            energy = self.parent.mi.get_value(self.parent.le_i1_energy)
        return energy



    def dispersion_measurement(self):
        beam_on = self.parent.orbit.read_orbit()
        if not beam_on and not self.parent.debug_mode:
            print("BEAM OFF")
            return

        self.parent.orbit.uncheck_red()

        self.orbit = self.parent.orbit.create_Orbit_obj()

        time_delay = self.ui.sb_time_delay.value()

        current_cav = self.ui.cb_cav_list.currentText()
        cav_id = "CTRL." + current_cav
        self.cavity = CavityA1(eid=cav_id, server=self.parent.server, subtrain=self.parent.subtrain)
        self.cavity.mi = self.parent.mi

        V_init = self.cavity.get_value()

        dV = self.ui.sb_voltage.value()
        n_steps = self.ui.sb_n_steps.value()

        volts_list = [V_init + dV*(i) for i in range(n_steps+1)]
        print(volts_list)
        multilines_x = self.setup_multi_plot(volts_list, self.plot_x, self.leg_x)
        multilines_y = self.setup_multi_plot(volts_list, self.plot_y, self.leg_y)
        print(len(multilines_x))
        bpms = self.parent.orbit.bpms
        bpms = self.parent.orbit.get_dev_from_cb_state(bpms)

        s_bpm = np.array([bpm.s for bpm in bpms])

        #x_mean_i, y_mean_i, x_std_i, y_std_i = self.get_orbit(bpms)

        #self.plot_orbits(multilines_x[0], s_bpm, x_mean_i)
        #self.plot_orbits(multilines_y[0], s_bpm, y_mean_i)
        X_mean = []
        Y_mean = []
        for i, v in enumerate(volts_list):
            self.cavity.set_value(v)
            print("set Voltage: ",  v)
            time.sleep(time_delay)
            x_mean, y_mean, x_std, y_std = self.get_orbit(bpms)
            X_mean.append(x_mean)
            Y_mean.append(y_mean)
            self.plot_orbits(multilines_x[i], s_bpm + self.parent.lat_zi, x_mean*1000)
            self.plot_orbits(multilines_y[i], s_bpm + self.parent.lat_zi, y_mean*1000)

        try:
            energy = self.get_section_energy()
        except:
            self.cavity.set_value(V_init)
            self.parent.error_box(message = "Can not read beam energy from the DOOCS. Cavity set value back.")
            return
        print("ENERGY = ", energy)
        dp_over_p = (volts_list[-1] - volts_list[0]) / energy
        if dp_over_p != 0:

            Dx = (X_mean[-1] - X_mean[0]) / dp_over_p
            Dy = (Y_mean[-1] - Y_mean[0]) / dp_over_p
        else:
            Dx = np.zeros_like(X_mean[0])
            Dy = np.zeros_like(Y_mean[0])

        self.cavity.set_value(V_init)


        self.set_disp2bpms(Dx, Dy, bpms, energy)

        Dx_des = np.array([bpm.Dx_des for bpm in bpms])
        Dy_des = np.array([bpm.Dy_des for bpm in bpms])

        self.plot_dispersion(s_bpm + self.parent.lat_zi, Dx, Dy, Dx_des, Dy_des)


    def calculate_disp(self, energy):
        Dx0, Dy0 = self.parent.orbit.orbit.response_matrix.method.read_virtual_dispersion(E0=energy)
        print("Dx0", Dx0)
        print("Dy0", Dy0)
        return Dx0, Dy0


    def set_disp2bpms(self, Dx, Dy, bpms, energy):

        Dx0, Dy0 = self.calculate_disp(energy)
        for i, bpm in enumerate(bpms):
            bpm.Dx = Dx[i]
            bpm.Dy = Dy[i]
            bpm.Dx_des = Dx0[i]
            bpm.Dy_des = Dy0[i]


    def add_orbit_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_x = win.addPlot(row=0, col=0)
        axis = self.plot_x.getAxis("bottom")
        axis.setStyle(showValues=False)
        # win.ci.layout.setRowMaximumHeight(0, 200)
        self.plot_x.showGrid(1, 1, 1)

        self.plot_y = win.addPlot(row=1, col=0)
        axis = self.plot_y.getAxis("bottom")
        axis.setStyle(showValues=False)

        self.plot_x.setXLink(self.plot_y)
        #self.plot_x.hideAxis("bottom")
        self.plot_x.setLabel('left', 'X Orbit', 'mm')
        self.plot_y.showGrid(1, 1, 1)
        self.plot_y.setLabel('left', 'Y Orbit', 'mm')
        self.plot_y.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()

        self.ui.w_disp.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)
        #legend for plot_x and plot_y
        self.leg_x = customLegend(offset=(75, 20))
        self.leg_x.setParentItem(self.plot_x.graphicsItem())

        self.leg_y = customLegend(offset=(75, 20))
        self.leg_y.setParentItem(self.plot_y.graphicsItem())

        self.plot_Dx = win.addPlot(row=2, col=0)
        self.plot_Dx.setLabel('left', 'Dx', 'm')
        axis = self.plot_Dx.getAxis("bottom")
        axis.setStyle(showValues=False)
        self.plot_Dy = win.addPlot(row=3, col=0)
        self.plot_Dy.setLabel('left', 'Dy', 'm')
        self.plot_Dy.showGrid(1, 1, 1)
        self.plot_Dy.setXLink(self.plot_y)
        #win.ci.layout.setRowMaximumHeight(2, 150)

        self.plot_Dx.setXLink(self.plot_y)
        self.plot_Dx.showGrid(1, 1, 1)

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.Dx_curve = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dx', antialias=True)
        self.plot_Dx.addItem(self.Dx_curve)
        self.plot_Dx.addLegend()

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=1)
        self.Dx_des_curve = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dx des', antialias=True)
        self.plot_Dx.addItem(self.Dx_des_curve)
        self.plot_Dx.addLegend()

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3, symbolPen='o')
        self.Dy_curve = pg.PlotDataItem(x=[], y=[], pen=pen, name='Dy', antialias=True)
        self.plot_Dy.addItem(self.Dy_curve)
        self.plot_Dy.addLegend()

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=1, symbolPen='o')
        self.Dy_des_curve = pg.PlotDataItem(x=[], y=[], pen=pen, name='Dy des', antialias=True)
        self.plot_Dy.addItem(self.Dy_des_curve)
        self.plot_Dy.addLegend()


    def setup_multi_plot(self, volts_list, plot, legend, ):
        """
        Reset plots when a new scan is started.
        """
        plot.clear()
        multilines = {}
        #self.plot_x.removeItem(self.orb_x_live)
    	#self.plot_y.removeItem(self.orb_y_live)
        #self.plot_x.legend.removeItem(self.orb_x_live.name())
        #self.plot_y.legend.removeItem(self.orb_y_live.name())


        #legend.scene().removeItem(legend)
        legend = customLegend(offset=(50, 10))
        legend.setParentItem(plot.graphicsItem())

        default_colors = [QtGui.QColor(255, 51, 51), QtGui.QColor(51, 255, 51), QtGui.QColor(255, 255, 51),QtGui.QColor(178, 102, 255)]
        for i, volt in enumerate(volts_list):

            #set the first 4 devices to have the same default colors
            if i < 4:
                color = default_colors[i]
            else:
                color = self.randColor()

            pen=pg.mkPen(color, width=2)
            multilines[i] = pg.PlotCurveItem([], [], pen=pen, antialias=True, name=str(volt))
            plot.addItem(multilines[i])
            legend.addItem(multilines[i], str(volt), color=str(color.name()))
        return multilines

    def randColor(self):
        """
        Generate random line color for each device plotted.
        :return: QColor object of a random color
        """
        hi = 255
        lo = 128
        c1 = np.random.randint(lo,hi)
        c2 = np.random.randint(lo,hi)
        c3 = np.random.randint(lo,hi)
        return QtGui.QColor(c1,c2,c3)

    def plot_orbits(self, line, s, y):
        line.setData(x=s, y = y)
        line.update()


    def plot_dispersion(self, s, Dx, Dy, Dx_des, Dy_des):
        s = s #+ self.parent.lat_zi
        self.Dx_curve.setData(x=s, y=Dx)
        self.Dy_curve.setData(x=s, y=Dy)
        self.Dx_curve.update()
        self.Dy_curve.update()

        self.Dx_des_curve.setData(x=s, y=Dx_des)
        self.Dy_des_curve.setData(x=s, y=Dy_des)
        self.Dx_des_curve.update()
        self.Dy_des_curve.update()


class customLegend(pg.LegendItem):
    """
    STUFF FOR PG CUSTOM LEGEND (subclassed from pyqtgraph).
    Class responsible for drawing a single item in a LegendItem (sans label).
    This may be subclassed to draw custom graphics in a Legend.
    """
    def __init__(self, size=None, offset=None):
        pg.LegendItem.__init__(self, size, offset)

    def addItem(self, item, name, color="CCFF00"):

        label = pg.LabelItem(name, color=color, size="6pt", bold=True)
        sample = None
        row = self.layout.rowCount()
        self.items.append((sample, label))
        self.layout.addItem(sample, row, 0)
        self.layout.addItem(label, row, 1)
        self.layout.setSpacing(0)


    """
    def dispersion_measurement_sim(self):
        self.create_Orbit_obj()
        disp_meas = LinacDisperseSimRM(lattice=copy.deepcopy(self.orbit.lat),
                                       hcors=copy.deepcopy(self.orbit.hcors),
                                    vcors=copy.deepcopy(self.orbit.vcors),
                                       bpms=copy.deepcopy(self.orbit.bpms))

        Dx0, Dy0 = disp_meas.read_virtual_dispersion(E0=self.parent.tws0.E)

        #print(Dx0)
        n_meas = 5
        x = np.zeros(len(self.orbit.bpms))
        y = np.zeros(len(self.orbit.bpms))
        for i in range(n_meas):
            for i, elem in enumerate(self.orbit.bpms):
                x_mm, y_mm = elem.mi.get_pos()
                x[i] += x_mm
                y[i] += y_mm
            time.sleep(0.2)
        x = x/n_meas
        y = y/n_meas

        V0 = self.cavity.get_value()
        dV = self.ui.sb_dV.value()
        V = V0 + dV
        self.cavity.set_value(V)
        time.sleep(4)
        x1 = np.zeros(len(self.orbit.bpms))
        y1 = np.zeros(len(self.orbit.bpms))
        for i in range(n_meas):
            for i, elem in enumerate(self.orbit.bpms):
                x_mm, y_mm = elem.mi.get_pos()
                x1[i] += x_mm
                y1[i] += y_mm
            time.sleep(0.2)
        x1 = x1 / n_meas
        y1 = y1 / n_meas
        dx = (x1 - x) / dV
        dy = (y1 - y) / dV

        for i, elem in enumerate(self.orbit.bpms):
            elem.Dx = dx[i]/1000
            elem.Dy = dy[i]/1000
            elem.Dx_des = Dx0[i]
            elem.Dy_des = Dy0[i]

        s_bpm = np.array([bpm.s for bpm in self.orbit.bpms]) + self.parent.lat_zi
        #x_bpm = np.array([bpm.Dx for bpm in self.orbit.bpms])*1000
        self.orb_x_ref.setData(x=s_bpm, y=dx)
        self.orb_x.setData(x=s_bpm, y=Dx0)
        self.orb_y_ref.setData(x=s_bpm, y=dy)
        self.orb_y.setData(x=s_bpm, y=Dy0)

        #self.plot_cor.update()
        self.orb_y.update()
        self.orb_x.update()
    """
