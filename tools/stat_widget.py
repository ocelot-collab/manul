"""
Sergey Tomin, XFEL/DESY, 2018
"""

import sys, os
from decimal import Decimal
import time
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

#from mint.xfel_interface import XFELMachineInterface, TestMachineInterface
#from machine_interface import *

#mi = XFELMachineInterface()
#mi = TestMachineInterface()




class Statistics():
    def __init__(self, device, npoints=100, delay=100):
        self.delay = delay
        self.N = npoints
        self.device = device
        self.clean()

        self.sigmas_title = "Sigma X/Y"
        self.x_hist_title = "X pos Distrib"
        self.y_hist_title = "Y pos Distrib"
        self.scatter_title = "Correlation"
        self.means_title = "Menas "
        
        
        #self.win = pg.GraphicsWindow()
        #self.win.resize(800, 800)
        #self.win.setWindowTitle('Photon beam pointing: XGM.2643.T9')
        #app = QtGui.QApplication([])
        self.win = pg.GraphicsView()
        self.layout = pg.GraphicsLayout(border=(100,100,100))
        self.win.setCentralItem(self.layout)
        self.win.show()
        self.win.setWindowTitle('pyqtgraph example: GraphicsLayout')
        self.win.resize(800,600)
        self.setup_ui()

        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        

    def clean(self):
        self.dx = []
        self.dy = []
        self.mean_x = []#np.empty(self.N)
        self.mean_y = []#np.empty(self.N)
        #self.spots = []
        self.sig_y = []#np.empty(self.N)
        self.sig_x = []#np.empty(self.N)
        self.cur_inx = 0
        self.start_time = time.time()

    def set_titles(self):
        self.scat_plot.setTitle(self.scatter_title)
        self.plot_x_hist.setTitle(self.x_hist_title)
        self.plot_y_hist.setTitle(self.y_hist_title)
        self.sigmas.setTitle(self.sigmas_title)
        self.means.setTitle(self.means_title)

    def setup_ui(self):

        self.plot_x_hist = self.layout.addPlot(row=0, col=0, rowspan=1, title=self.x_hist_title)
        #self.layout
        
        self.plot_x_hist.showGrid(1, 1, 1)
        self.plot_x_hist.hideAxis('bottom')
        self.data_hist_x = pg.PlotDataItem([0,0], [0], stepMode=True, fillLevel=0, brush=(255, 0, 0, 100))

        self.plot_x_hist.addItem(self.data_hist_x)
        
        self.scat_plot = self.layout.addPlot(row=1, col=0, rowspan=1, title=self.scatter_title)
        self.scat_plot.showGrid(1, 1, 1)
        self.scat_plot.setXLink(self.plot_x_hist)
        
        self.plot_y_hist = self.layout.addPlot(row=1, col=1, rowspan=1, title=self.y_hist_title)
        self.plot_y_hist.showGrid(1, 1, 1)
        self.plot_y_hist.hideAxis('left')


        self.layout2 = self.layout.addLayout(row=0, col=1)

        self.sigmas = self.layout2.addPlot(row=0, col=0, rowspan=1,title=self.sigmas_title)
        self.sigmas.showGrid(1, 1, 1)
        self.sigmas.hideAxis('bottom')
        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4)
        self.plt_sig_x = pg.PlotDataItem(x=[], y=[], pen=pen, symbol=None, name='X', antialias=True)
        self.sigmas.addItem(self.plt_sig_x )
        
        
        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=4)
        self.plt_sig_y = pg.PlotDataItem(x=[], y=[], pen=pen, symbol=None, name='Y', antialias=True)
        self.sigmas.addItem(self.plt_sig_y )
        
        
        
        self.means = self.layout2.addPlot(row=1, col=0, rowspan=1,title=self.means_title)
        self.means.showGrid(1, 1, 1)
        #self.p11 = self.means.plotItem
        
        #self.means_y = pg.ViewBox()
        #a1 = pg.AxisItem("right")
        #self.means.showAxis('right')
        #self.layout2.scene().addItem(self.means_y)
        #a1.linkToView(self.means_y)
        #self.means.getAxis('right').linkToView(self.means_y)
        #self.means_y.setXLink(self.means)
        #self.means_y.setYRange(-10,10)
        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4)
        self.plt_mean_x = pg.PlotDataItem(x=[], y=[], pen=pen, symbol=None, name='X', antialias=True)
        self.means.addItem(self.plt_mean_x )
        
        
        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=4)
        self.plt_mean_y = pg.PlotDataItem(x=[], y=[], pen=pen, symbol=None, name='Y', antialias=True)
        self.means.addItem(self.plt_mean_y )

        self.means.setXLink(self.sigmas)
        
        #sigmas.addLegend()
        
        self.data_hist_y = pg.PlotDataItem([0,0], [0], stepMode=True, fillLevel=0, brush=(255, 255, 0, 200))
        self.data_hist_y.rotate(-90)
        self.plot_y_hist.addItem(self.data_hist_y)
        self.plot_y_hist.setYLink(self.scat_plot)
        
        
        
        self.scatter = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 100, 255, 120))
        #color = QtGui.QColor(255, 0, 0)
        #pen = pg.mkPen(color, width=2)
        #self.drift_scatter = pg.PlotDataItem(x=[], y=[], pen=pen, symbol="o",symbolPen=(200,200,200),
        #    symbolBrush=(255, 0, 0), name='Y', antialias=True)
        #self.drift_scatter = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None), brush=pg.mkBrush(255, 0, 0, 200))
        self.scat_plot.addItem(self.scatter)
        #self.scat_plot.addItem(self.drift_scatter)
    
    def scroll_graph(self, data, x, plt_wdgt):
        #if self.cur_inx >= data.shape[0]:
#
        #    #tmp = np.copy(data)
        #    print(self.cur_inx, data)
        #    data = np.append(data, np.zeros(data.shape[0]))
        #
        #    #data[:tmp.shape[0]] = tmp[:]
        #    print(self.cur_inx, data)
        #data[self.cur_inx] = x
        #datay = data[:self.cur_inx]
        #print(datay)
        data.append(x)
        plt_wdgt.setPos(-self.cur_inx, 0)
        #print(data)
        plt_wdgt.setData(np.arange(len(data)), data)

    def update(self):
        #global dx, dy, spots, i, sig_y, sig_x
        try:
            x = self.device.get_x()
            y = self.device.get_y()
            #print(x, y)
        except Exception as e:
            print("doocs error", str(e))
            time.sleep(1)
            return 
        if len(self.dx) > self.N:
            self.dx = np.delete(self.dx, 0)
            self.dy = np.delete(self.dy, 0)



        self.dx = np.append(self.dx, x)
        self.dy = np.append(self.dy, y)
        
        
        y_hist, x_hist = np.histogram(self.dx, bins=100)
        y_hist_y, x_hist_y = np.histogram(self.dy, bins=100)
        
        self.scatter.setData(self.dx, self.dy)
        self.data_hist_y.setData(-x_hist_y, y_hist_y)
        self.data_hist_x.setData(x_hist, y_hist)
        
        sigy = np.std(self.dy)
        my = np.mean(self.dy)
        
        sigx = np.std(self.dx)
        mx = np.mean(self.dx)
        #if self.cur_inx > 10 and  self.cur_inx % 10 == 0:
        #self.mean_y.append(my)
        #self.mean_x.append(mx)
        
        #self.drift_scatter.setData(self.mean_x, self.mean_y)


        self.scroll_graph(self.sig_y, sigy, self.plt_sig_y)
        self.scroll_graph(self.sig_x, sigx, self.plt_sig_x)
        
        self.scroll_graph(self.mean_x, mx, self.plt_mean_x)
        self.scroll_graph(self.mean_y, my, self.plt_mean_y)
        
        #txt_sigma_x.setText("sigma_x="+'%.2E' % Decimal(str(sigx)))

        self.cur_inx += 1

    def start(self):
        self.clean()
        self.sigmas.setRange(xRange=[-self.N, 0])
        self.means.setRange(xRange=[-self.N, 0])
        self.timer.start(self.delay)

    def stop(self):
        self.timer.stop()


#timer_bc1 = pg.QtCore.QTimer()
#timer_bc1.timeout.connect(update_bc1)
#timer_bc1.start(100)

#timer_bc2 = pg.QtCore.QTimer()
#timer_bc2.timeout.connect(update_bc2)
#timer_bc2.start(100)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
