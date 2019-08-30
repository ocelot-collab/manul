import numpy as np
import time
from threading import Thread
from machine_interface import *

mi = XFELMachineInterface()
#mi = TestMachineInterface()

class Write10Hz(Thread):
    def __init__(self, mi):
        super(Write10Hz, self).__init__()
        self.indx = 0
        self.nentries = 1000
        self.delay = 0.1
        self.kill = False
        self.mi = mi
        self.filename_con = "data_10Hz_screen"
        self.filename = self.filename_con + "_0"
        self.clean_data()
        self.n_subfile = 0
        self.ndata_max = 10000

    def clean_data(self):
        self.pointing = []
        self.x_orbits = []
        self.y_orbits = []
        self.orb_times = []
        self.energy = []
        self.fb = []

    def get_fb(self):
        status = self.mi.get_value("XFEL.FEEDBACK/ORBIT.SA1/ORBITFEEDBACK/ACTIVATE_FB")
        return status

    def get_orbit(self):
        now = time.time()
        orbit_x = self.mi.get_value("XFEL.DIAG/BPM/*.SA1/X.ALL")
        orbit_y = self.mi.get_value("XFEL.DIAG/BPM/*.SA1/Y.ALL")
        x = [bpm["float1"] for bpm in orbit_x]
        #names = [bpm["str"] for bpm in orbit_x]
        y = [bpm["float1"] for bpm in orbit_y]
        names = [bpm["str"] for bpm in orbit_x]
        return x, y, names, now

    def get_pointing(self):
        x_26 = self.mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/Y.TD")[0][1]
        y_26 = self.mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/X.TD")[0][1]
        x_33 = self.mi.get_value("XFEL.FEL/XGM/XGM.3311.T9/Y.TD")[0][1]
        y_33 = self.mi.get_value("XFEL.FEL/XGM/XGM.3311.T9/X.TD")[0][1]
        now = time.time()
        return now, x_26, y_26, x_33, y_33

    def get_energy(self):
        cl = self.mi.get_value("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/CL/ENERGY.ALL")
        t4 = self.mi.get_value("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/T4/ENERGY.ALL")
        now = time.time()
        return now, cl, t4

    def read(self):
        try:
            x, y, names, now = self.get_orbit()
            self.x_orbits.append(x)
            self.y_orbits.append(y)
            self.orb_times.append(now)

            now, x_26, y_26, x_33, y_33 = self.get_pointing()
            self.pointing.append([now, x_26, y_26, x_33, y_33])

            now, cl, t4 = self.get_energy()
            self.energy.append([now, cl, t4])

            status = self.get_fb()
            self.fb.append(status)

            self.indx += 1
        except Exception as e:
            print("ERROR: ", str(e))

        # print("indx = ", self.indx)
        if self.indx > 0 and self.indx % self.nentries == 0:
            print("save", len(self.x_orbits), "dT = ", time.time() - self.start)
            np.savez(self.filename + ".npz", orbit_x=self.x_orbits, orbit_y=self.y_orbits,
                     orbit_time=self.orb_times, pointing=self.pointing, bpm_names=names, fb_status=self.fb, energy=self.energy)
            self.start = time.time()

        if self.indx > 0 and self.indx % self.ndata_max == 0:
            self.n_subfile += 1
            self.filename = self.filename_con + "_" + str(self.n_subfile)
            print("new_file: ", self.filename)
            self.clean_data()

    def run(self):
        print("run")
        self.start = time.time()
        while not self.kill:
            # print("here")
            self.read()

            time.sleep(self.delay)



write10Hz = Write10Hz(mi)
write10Hz.start()
