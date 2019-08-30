
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from pyqtgraph.dockarea import *
from stat_widget import *
from machine_interface import *

#mi = XFELMachineInterface()
mi = TestMachineInterface()


class Device:
    def __init__(self):
        self.mi = mi
    def get_x(self):
       #x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.2643.T9/IX.POS")
       x = mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/X.TD")[0][1]
       return x

    def get_y(self):
       #x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.2643.T9/IY.POS")
       x = mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/Y.TD")[0][1]
       return x

class Dev3311(Device):
    def __init__(self):
       Device.__init__(self)

    def get_x(self):
        #x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.3311.T9/IX.POS")
        x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.2643.T9/IX.POS")
        # x = mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/X.TD")[0][1]
        return x

    def get_y(self):
        #x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.3311.T9/IY.POS")
        x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.2643.T9/IY.POS")
        # x = mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/Y.TD")[0][1]
        return x


class DevEnergy(Device):
    def __init__(self):
        Device.__init__(self)

    def get_x(self):
        #x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.3311.T9/IX.POS")
        x = mi.get_value("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/CL/ENERGY.ALL")
        # x = mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/X.TD")[0][1]
        return x

    def get_y(self):
        #x = self.mi.get_value("XFEL.FEL/XGM.POSMON/XGM.3311.T9/IY.POS")
        x = mi.get_value("XFEL.DIAG/BEAM_ENERGY_MEASUREMENT/T4/ENERGY.ALL")
        # x = mi.get_value("XFEL.FEL/XGM/XGM.2643.T9/Y.TD")[0][1]
        return x

class MyDock(Dock):
    def __init__(self,*args,**kwargs):
        super(MyDock, self).__init__(*args,**kwargs)
        
    def close(self):
        """Remove this dock from the DockArea it lives inside."""
        print("sfadfs")
        self.setParent(None)
        self.label.setParent(None)
        self._container.apoptose()
        self._container = None
        
        self.sigClosed.emit(self)

dev_energy = DevEnergy()

dev2643 = Device()
dev3311 = Dev3311()


app = QtGui.QApplication([])
window = QtGui.QMainWindow()
area = DockArea()
window.setCentralWidget(area)
window.resize(1200,800)
window.setWindowTitle('pyqtgraph example: dockarea')

d1 = Dock("XGM.2643.T9", size=(8, 4))
area.addDock(d1, 'left')

d2 = MyDock("XGM.2643.T9 SLOW", size=(8, 4))
area.addDock(d2, 'right')

d3 = Dock("Controls", size=(1, 1))
area.addDock(d3, 'right')

d4 = Dock("Energy Spread", size=(8, 4))
area.addDock(d4, 'left')


pointing2643 = Statistics(device=dev2643, npoints=100, delay=100)

d1.addWidget(pointing2643.win)

pointing3311 = Statistics(device=dev3311, npoints=100, delay=100)

d2.addWidget(pointing3311.win)

energy_spread = Statistics(device=dev_energy, npoints=100, delay=100)

energy_spread.sigmas_title = "RMS CL/T4"
energy_spread.x_hist_title = "CL Energy Distrib"
energy_spread.y_hist_title = "T4 Energy Distrib"
energy_spread.scatter_title = "Correlation CL/T4"
energy_spread.set_titles()
d4.addWidget(energy_spread.win)


def start():
    pointing2643.N = s4.value()
    pointing3311.N = s4.value()
    energy_spread.N = s4.value()

    pointing2643.delay = s3.value()*1000
    pointing3311.delay = 1000#s3.value()*1000
    energy_spread.delay = s3.value() * 1000

    print(pointing2643.N , pointing2643.delay)
    #pointing3311.start()
    #pointing2643.start()
    energy_spread.start()

def stop():
    pointing3311.stop()
    pointing2643.stop()
    energy_spread.stop()
## first dock gets save/restore buttons
w1 = pg.LayoutWidget()
label = QtGui.QLabel(""" 
""")
start_btn = QtGui.QPushButton('Start Statistics')
stop_btn = QtGui.QPushButton('Stop Statistics')
#s3 = pg.SpinBox(value=100, dec=True, step=10, minStep=1e-6, bounds=[10, 10000], suffix='sec', siPrefix=True)
s3 = pg.SpinBox(value=0.1, step=0.1, suffix='sec',bounds=[0.001, 10], siPrefix=True)
s4 = pg.SpinBox(value=500, int=True, dec=True, minStep=1, bounds=[100, 5000], step=1, decimals=4)
#stop_btn.setEnabled(False)
#w1.addWidget(label, row=0, col=0)
w1.addWidget(s3, row=0, col=0)
w1.addWidget(s4, row=1, col=0)
w1.addWidget(start_btn, row=2, col=0)
w1.addWidget(stop_btn, row=3, col=0)
d3.addWidget(w1)
start_btn.clicked.connect(start)
stop_btn.clicked.connect(stop)
window.show()

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
