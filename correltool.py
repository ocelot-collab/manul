#!/opt/anaconda4/bin/python
"""
Sergey Tomin. XFEL/DESY, 2017.
"""
#QT imports
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QFrame, QMessageBox, QMainWindow, QDialog
#normal imports
import numpy as np
#import epics
import sys
import os


path = os.path.realpath(__file__)
indx = path.find("manul")
print("PATH", os.path.realpath(__file__), path[:indx])
sys.path.append(path[:indx])
if sys.version_info[0] == 2:
    from imp import reload
else:
    from importlib import reload
import time
import pyqtgraph as pg
from gui.uicorrelation import *
from ocelot.optimizer.mint.xfel_interface import *


class ManulInterfaceWindow(QMainWindow, Ui_MainWindow):
    """ Main class for the GUI application """
    def __init__(self):
        """
        Initialize the GUI and QT UI aspects of the application.
        Initialize the scan parameters.
        Connect start and logbook buttons on the scan panel.
        Initialize the plotting.
        Make the timer object that updates GUI on clock cycle during a scan.
        """
        super(ManulInterfaceWindow, self).__init__()
        #Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # load in the dark theme style sheet
        self.loadStyleSheet()

        path = os.path.realpath(__file__)
        indx = path.find("ocelot" + os.sep + "optimizer")
        self.path2ocelot = path[:indx]
        self.path2manul = path[:path.find("manul")]
        print("path to manul", self.path2manul)
        self.optimizer_path = self.path2ocelot + "ocelot" + os.sep + "optimizer" + os.sep
        self.config_dir = self.path2ocelot + "config_optim" +os.sep
        self.gold_orbits_dir = self.path2manul + "manul" + os.sep + "golden_orbits" + os.sep
        self.gold_orbits_from_OD_dir = "/home/xfeloper/data/orbit_display/"#self.path2manul + "manul" + os.sep + "golden_orbits" + os.sep
        self.rm_files_dir = self.path2manul + "manul" + os.sep + "rm_files" + os.sep
        self.set_file = self.config_dir + "default.json" # ./parameters/default.json"
        self.obj_func_path = self.optimizer_path + "mint" + os.sep + "obj_function.py"
        self.obj_save_path = self.config_dir +  "obj_funcs" + os.sep
        # initialize
        #QFrame.__init__(self)


        self.logbook = "xfellog"

        self.mi = XFELMachineInterface()
        #self.mi = TestMachineInterface()


        #load in the dark theme style sheet
        self.loadStyleSheet()

        self.cb_energy_ch.addItem("CL")
        self.cb_energy_ch.addItem("T4D")
        self.cb_energy_ch.addItem("TLD")
        self.cb_energy_ch.addItem("T4")
        self.cb_energy_ch.setCurrentIndex(2)


        self.statistics_timer = pg.QtCore.QTimer()
        self.statistics_timer.timeout.connect(self.loop)
        
        self.cb_disp.setChecked(True)
        self.cb_sase.setChecked(True)
        self.cb_disp.stateChanged.connect(self.disp_line)
        self.cb_sase.stateChanged.connect(self.sase_line)
        self.pb_statistics_start.clicked.connect(self.start_stop_statistics)
        self.add_orbit_plot()

    def disp_line(self):
        if not self.cb_disp.isChecked():
            self.plot_x.removeItem(self.orb_x_disp)
            self.plot_y.removeItem(self.orb_y_disp)
            self.plot_x.legend.removeItem(self.orb_x_disp.name())
            self.plot_y.legend.removeItem(self.orb_y_disp.name())

        else:
            self.plot_x.addItem(self.orb_x_disp)
            self.plot_y.addItem(self.orb_y_disp)

    def sase_line(self):
        if not self.cb_sase.isChecked():
            self.plot_x.removeItem(self.orb_x)
            self.plot_y.removeItem(self.orb_y)
            self.plot_x.legend.removeItem(self.orb_x.name())
            self.plot_y.legend.removeItem(self.orb_y.name())

        else:
            self.plot_x.addItem(self.orb_x)
            self.plot_y.addItem(self.orb_y)


    def read_once(self, i):
        #start = time.time()
        try:
            sase = pydoocs.read("XFEL.FEL/XGM.PREPROCESSING/XGM.2643.T9.CH0/RESULT.TD")["data"]
            sase = np.mean(sase)
            if self.cb_energy_ch.currentText() == "CL":
                energy_ch = pydoocs.read("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/CL/ENERGY.ALL")["data"]
            elif self.cb_energy_ch.currentText() == "T4D":
                energy_ch = pydoocs.read("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/T4D/ENERGY.ALL")["data"]
            elif self.cb_energy_ch.currentText() == "TLD":
                energy_ch = pydoocs.read("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/TLD/ENERGY.ALL")["data"]
            elif self.cb_energy_ch.currentText() == "T4":
                energy_ch = pydoocs.read("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/T4/ENERGY.ALL")["data"]
            else:
                print("Wrong Energy Channel")
                
                energy_ch = 0

            orbit_x = pydoocs.read("XFEL.DIAG/ORBIT/*/X.ALL")
            orbit_y = pydoocs.read("XFEL.DIAG/ORBIT/*/Y.ALL")
        except:
            self.error_box("Error during reading from DOOCS.")
            return False 
        self.sase_array[i] = sase
        self.energy_array[i] = energy_ch
        values_x = np.array([data[1] for data in orbit_x["data"]])
        values_y = np.array([data[1] for data in orbit_y["data"]])
        #names = [data["str"] for data in orbit["data"]]
        self.bpms_x[:,i] = values_x[:]
        self.bpms_y[:,i] = values_y[:]
        return True
        #print(sase, values_x[100])

    def correl_matrix(self, x, y):
        x_var = x - np.mean(x)
        y_var = y - np.mean(y)
        correl = np.mean(x_var * y_var)/np.std(x_var)/np.std(y_var)
        #if not np.any(x_var) or not np.any(x_var):
        #    print("wrong orbit reasing")
        return correl

    def correl_least(self, x, y):
        x_var = x - np.mean(x)
        y_var = y - np.mean(y)
        #print("x_var", x_var)
        #print("y_var", y_var)
        if not np.any(x_var) or not np.any(x_var):
            #print("wrong orbit reasing")
            return 0
            
        a = np.vstack([x_var, np.ones(len(x_var))]).T
        res = np.dot(np.linalg.inv(np.dot(a.T, a)), np.dot(a.T, y_var))
        return res[0]

    def calculate_correlation(self, n_real_readings):
        sase_array = np.array(self.sase_array)[:n_real_readings]
        energy_array = np.array(self.energy_array)[:n_real_readings]
        corelation_x = []
        corelation_y = []
        e_corelation_x = []
        e_corelation_y = []
        for n_bpm in range(self.n_bpms):
            
            bpm_x = self.bpms_x[n_bpm][:n_real_readings]
            bpm_y = self.bpms_y[n_bpm][:n_real_readings]
            #print("corelation_x")
            corelation_x.append(self.correl_matrix(x=bpm_x, y=sase_array))
            #print("corelation_y")
            corelation_y.append(self.correl_matrix(x=bpm_y, y=sase_array))
            #print("corelation_xe")
            e_corelation_x.append(self.correl_matrix(x=bpm_x, y=energy_array))
            #print("corelation_ye")
            e_corelation_y.append(self.correl_matrix(x=bpm_y, y=energy_array))
        sase_correl_x = np.array(corelation_x)
        sase_correl_y = np.array(corelation_y)
        e_correl_x = np.array(e_corelation_x)
        e_correl_y = np.array(e_corelation_y)
        
        disp_coef = 0.12/e_correl_x[self.bpm_index]
            
        if self.cb_sase.isChecked():
            self.orb_x.setData(x=np.arange(self.n_bpms), y=sase_correl_x*disp_coef)
            self.orb_y.setData(x=np.arange(self.n_bpms), y=sase_correl_y*disp_coef)

        if self.cb_disp.isChecked():
            self.orb_x_disp.setData(x=np.arange(self.n_bpms), y=e_correl_x*disp_coef)
            self.orb_y_disp.setData(x=np.arange(self.n_bpms), y=e_correl_y*disp_coef)
            
    def loop(self):
        
        ok = self.read_once(self.counter)
        if not ok:
            self.stop_statistics()
        self.counter += 1
        self.n_real_readings += 1
        print(self.counter)
        ration = int(self.sb_update_rate.value()*10)
        if self.counter % ration == ration - 1:
            self.calculate_correlation(self.n_real_readings)
        if self.counter == self.sb_n_shots.value():
            self.counter = 0
            self.n_real_readings = int(self.sb_n_shots.value()-1)
        #self.orb_y.setData(x=self.orbit_s, y=delta_ro_x*1000)
        #self.orb_x.setData(x=self.orbit_s, y=delta_ro_y*1000)

    def stop_statistics(self):
        self.statistics_timer.stop()
        self.pb_statistics_start.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_statistics_start.setText("Statistics Accum On")

    def start_stop_statistics(self):
        """
        Method to start/stop feedback timer.
        sb_feedback_sec - spinBox - set seconds for timer
        pb_feedback - pushBatton Off/On
        feedback_timer - timer
        :return:
        """
        #print("I am here")
        self.nreadings = int(self.sb_n_shots.value())
        self.counter = 0
        self.n_real_readings = 0
        #delay = self.sb_update_rate.value()*1000
        orbit = pydoocs.read("XFEL.DIAG/ORBIT/*/X.ALL")
        values = np.array([data[1] for data in orbit["data"]])
        names = [data[4] for data in orbit["data"]]

        indx_bpma_2591 = names.index("BPMA.2591.T4")
        self.bpm_index = indx_bpma_2591
        self.n_bpms = len(names)
        #n_readings = 100
        
        self.bpms_x = np.zeros((self.n_bpms, self.nreadings))
        self.bpms_y = np.zeros((self.n_bpms, self.nreadings))
        self.sase_array = np.zeros(self.nreadings)
        self.energy_array = np.zeros(self.nreadings)

        if self.pb_statistics_start.text() == "Statistics Accum Off":
            self.statistics_timer.stop()
            #self.stat_thread.stop()
            self.pb_statistics_start.setStyleSheet("color: rgb(85, 255, 127);")
            self.pb_statistics_start.setText("Statistics Accum On")
        else:

            self.statistics_timer.start(100)
            self.statistics_timer.start()
            self.pb_statistics_start.setText("Statistics Accum Off")
            self.pb_statistics_start.setStyleSheet("color: red")

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
        self.w_orbit.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='SASE correl', antialias=True)
        self.plot_y.addItem(self.orb_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.orb_y_disp = pg.PlotDataItem(x=[], y=[], pen=pen, name='Dispersion', antialias=True)
        self.plot_y.addItem(self.orb_y_disp)

        self.plot_x.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen,  name='SASE correl', antialias=True)

        self.plot_x.addItem(self.orb_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3, symbolPen='o')
        #self.orb_x_disp = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Dispersion', antialias=True)
        self.orb_x_disp = pg.PlotDataItem(x=[], y=[], pen=pen, name='Dispersion', antialias=True)
        self.plot_x.addItem(self.orb_x_disp)
        #self.plot_x.addLegend()
        #self.plot_x.setYRange(-2, 2)
        #self.plot_y.setYRange(-2, 2)


 


    def zoom_signal(self):
        #s = self.plot1.viewRange()[0][0]
        #s_pos = np.array([q.s_pos for q in self.quads])
        s_pos = np.array([q.s_pos for q in self.quads]) + self.lat_zi
        s_up = self.plot1.viewRange()[0][0]
        s_down = self.plot1.viewRange()[0][1]
        s_up = s_up if s_up <= s_pos[-1] else s_pos[-1]
        s_down = s_down if s_down >= s_pos[0] else s_pos[0]

        indexes = np.arange(np.argwhere(s_pos >= s_up)[0][0], np.argwhere(s_pos <= s_down)[-1][0] + 1)
        mask = np.ones(len(self.quads), np.bool)
        mask[indexes] = 0
        self.quads = np.array(self.quads)
        [q.ui.set_hide(hide=False) for q in self.quads[indexes]]
        [q.ui.set_hide(hide=True) for q in self.quads[mask]]


    def add_plot(self):

        win = pg.GraphicsLayoutWidget()

        self.plot3 = win.addPlot(row=0, col=0)
        win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot3.showGrid(1, 1, 1)


        self.plot1 = win.addPlot(row=1, col=0)
        self.plot3.setXLink(self.plot1)

        self.plot1.showGrid(1, 1, 1)

        self.plot1.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        self.ui.widget_2.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot1.setAutoVisible(y=True)

        self.plot1.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.beta_x = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        self.plot1.addItem(self.beta_x)

        pen = pg.mkPen(color, width=1)
        self.beta_x_des = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        self.plot1.addItem(self.beta_x_des)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.beta_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        self.plot1.addItem(self.beta_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=1)
        self.beta_y_des = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        self.plot1.addItem(self.beta_y_des)

        self.plot2 = win.addPlot(row=2, col=0)
        win.ci.layout.setRowMaximumHeight(2, 150)

        self.plot2.setXLink(self.plot1)
        self.plot2.showGrid(1, 1, 1)

        self.plot3.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.Dx = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dx', antialias=True)
        self.plot3.addItem(self.Dx)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.Dy = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dy', antialias=True)
        self.plot3.addItem(self.Dy)
        self.plot2.sigRangeChanged.connect(self.zoom_signal)

    def error_box(self, message):
        QtGui.QMessageBox.about(self, "Error box", message)

    def question_box(self, message):
        #QtGui.QMessageBox.question(self, "Question box", message)
        reply = QtGui.QMessageBox.question(self, "Recalculate ORM?",
                "Recalculate Orbit Response Matrix?",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            return True

        return False

    def update_plot(self, s, bx, by, dx, dy):
        # Line
        s = np.array(s) + self.lat_zi
        self.beta_x.setData(x=s, y=bx)
        self.beta_y.setData(x=s, y=by)
        self.plot1.update()
        #self.plot1.setYRange(-5, 200)
        self.plot2.update()
        self.Dx.setData(x=s, y=dx)
        self.Dy.setData(x=s, y=dy)
        self.plot3.update()


    def loadStyleSheet(self):
        """ Sets the dark GUI theme from a css file."""
        try:
            self.cssfile = "gui/colinDark.css"
            with open(self.cssfile, "r") as f:
                self.setStyleSheet(f.read())
        except IOError:
            print ('No style sheet found!')




def main():


    #make pyqt threadsafe
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    #create the application
    app    = QApplication(sys.argv)


    window = ManulInterfaceWindow()


    #show app
    window.setWindowIcon(QtGui.QIcon('manul.png'))

    window.show()
    window.raise_()
    #Build documentaiton if source files have changed
    # TODO: make more universal
    #os.system("cd ./docs && xterm -T 'Ocelot Doc Builder' -e 'bash checkDocBuild.sh' &")
    #exit script
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
    #window = ManulInterfaceWindow()
    #window.read_quads()
