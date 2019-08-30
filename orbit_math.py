"""
S.Tomin, 2018, DESY/XFEL. Prototype of a class with all orbit correction math
"""
import numpy as np
from threading import Thread, Event
import logging


logger = logging.getLogger(__name__)


class OrbitReader(Thread):
    def __init__(self, parent):
        super(OrbitReader, self).__init__()
        self.parent = parent

    def read_correctors(self, corrs):
        """
        Method to read from MI correctors (angles: mrad->rad)
        self.online_calc = False - switch off recalculating of the calculated orbit
        otherwise after every set in table orbit will be recalculated.

        :return:
        """
        self.online_calc = False

        for elem in corrs:
            elem.kick_mrad = elem.mi.get_value()
            elem.angle_read = elem.kick_mrad * 1e-3
            elem.i_kick = elem.kick_mrad
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)

        self.online_calc = True
        self.parent.lat.update_transfer_maps()

    def read_bpms(self, bpms):

        """
        Method to read from MI: correctors (angles: mrad->rad) and
        BPMs (X and Y: mm -> m) and checks charge on the BPMs
        if the charge below charge_thresh return False

        :return: bool, True if the charge on all BPMs >= charge_thresh otherwise False
        """

        charge_thresh = 0.005

        #bpms = self.get_dev_from_cb_state(self.bpms)

        beam_on = True
        for elem in bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                if np.isnan(x_mm) or np.isnan(y_mm):
                    logger.warning("read bpm: " + elem.id + "NaN -> was unchecked")
                    elem.ui.uncheck()
                charge = elem.mi.get_charge()
                if charge < charge_thresh:
                    beam_on = False
                # print(elem.id, "bunch charge: ", self.parent.bunch_charge, "   charge_tol:", self.parent.charge_tol, "charge: ", charge, np.abs(charge/self.parent.bunch_charge) < self.parent.charge_tol/100)
                if np.abs(charge / self.parent.bunch_charge) < self.parent.charge_tol / 100:
                    logger.info(" BPM:" + elem.id + " unchecked -> " + str(np.round(charge, 2)) + "/" + str(
                        np.round(self.parent.bunch_charge, 2)) + " < " + str(self.parent.charge_tol / 100))
                    elem.ui.uncheck()
                elem.x = x_mm / 1000.
                elem.y = y_mm / 1000.
                elem.ui.set_value((x_mm, y_mm))
            except:
                logger.error("read bpm: " + elem.id + "ERROR during reading -> was unchecked ")
                elem.ui.uncheck()
        # beam_on = self.read_bpms(n_readings=1, n_last_readings=1)
        # self.update_cors_plot()
        return beam_on

    def read_orbit(self, corrs, bpms):
        self.read_correctors(corrs)
        beam_on = self.read_bpms(bpms)
        self.update_plot()
