# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIAdviser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1196, 921)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #Form.setStyleSheet("background-color: white")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pb_read_from_mf = QtWidgets.QPushButton(self.tab)
        self.pb_read_from_mf.setEnabled(False)
        self.pb_read_from_mf.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pb_read_from_mf.setFont(font)
        self.pb_read_from_mf.setObjectName("pb_read_from_mf")
        self.gridLayout_11.addWidget(self.pb_read_from_mf, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lab_sase_max = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_sase_max.sizePolicy().hasHeightForWidth())
        self.lab_sase_max.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_sase_max.setFont(font)
        self.lab_sase_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_sase_max.setObjectName("lab_sase_max")
        self.gridLayout_4.addWidget(self.lab_sase_max, 7, 3, 1, 1)
        self.lab_sase_min = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_sase_min.sizePolicy().hasHeightForWidth())
        self.lab_sase_min.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_sase_min.setFont(font)
        self.lab_sase_min.setObjectName("lab_sase_min")
        self.gridLayout_4.addWidget(self.lab_sase_min, 7, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_4.addWidget(self.horizontalSlider, 6, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 7, 2, 1, 1)
        self.lab_sase_cur = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_sase_cur.sizePolicy().hasHeightForWidth())
        self.lab_sase_cur.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_sase_cur.setFont(font)
        self.lab_sase_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sase_cur.setObjectName("lab_sase_cur")
        self.gridLayout_4.addWidget(self.lab_sase_cur, 5, 2, 1, 1)
        self.lab_nfiles = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_nfiles.sizePolicy().hasHeightForWidth())
        self.lab_nfiles.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_nfiles.setFont(font)
        self.lab_nfiles.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_nfiles.setObjectName("lab_nfiles")
        self.gridLayout_4.addWidget(self.lab_nfiles, 9, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 9, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 8, 0, 1, 4)
        self.gridLayout_11.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_find_go_2 = QtWidgets.QPushButton(self.tab)
        self.pb_find_go_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pb_find_go_2.setFont(font)
        self.pb_find_go_2.setObjectName("pb_find_go_2")
        self.horizontalLayout.addWidget(self.pb_find_go_2)
        self.pb_find_go = QtWidgets.QPushButton(self.tab)
        self.pb_find_go.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pb_find_go.setFont(font)
        self.pb_find_go.setObjectName("pb_find_go")
        self.horizontalLayout.addWidget(self.pb_find_go)
        self.gridLayout_11.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.rb_x_plane = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_x_plane.setFont(font)
        self.rb_x_plane.setChecked(True)
        self.rb_x_plane.setObjectName("rb_x_plane")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.rb_x_plane)
        self.gridLayout.addWidget(self.rb_x_plane, 0, 0, 1, 1)
        self.rb_yplane = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_yplane.setFont(font)
        self.rb_yplane.setObjectName("rb_yplane")
        self.buttonGroup_2.addButton(self.rb_yplane)
        self.gridLayout.addWidget(self.rb_yplane, 0, 1, 1, 1)
        self.pb_show = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_show.setFont(font)
        self.pb_show.setObjectName("pb_show")
        self.gridLayout.addWidget(self.pb_show, 0, 2, 1, 1)
        self.plot_widget = OclMonitor(self.groupBox_3)
        self.plot_widget.setMinimumSize(QtCore.QSize(0, 400))
        self.plot_widget.setObjectName("plot_widget")
        self.gridLayout.addWidget(self.plot_widget, 1, 0, 1, 3)
        self.plot_widget.raise_()
        self.rb_x_plane.raise_()
        self.rb_yplane.raise_()
        self.pb_show.raise_()
        self.gridLayout_11.addWidget(self.groupBox_3, 5, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 3, 0, 1, 1)
        self.sb_nneighbors = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_nneighbors.sizePolicy().hasHeightForWidth())
        self.sb_nneighbors.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sb_nneighbors.setFont(font)
        self.sb_nneighbors.setMaximum(20)
        self.sb_nneighbors.setSingleStep(1)
        self.sb_nneighbors.setProperty("value", 1)
        self.sb_nneighbors.setObjectName("sb_nneighbors")
        self.gridLayout_6.addWidget(self.sb_nneighbors, 3, 1, 1, 1)
        self.rb_energy_prof = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_energy_prof.setFont(font)
        self.rb_energy_prof.setChecked(True)
        self.rb_energy_prof.setObjectName("rb_energy_prof")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_energy_prof)
        self.gridLayout_6.addWidget(self.rb_energy_prof, 0, 0, 1, 1)
        self.rb_cor_kick = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_cor_kick.setFont(font)
        self.rb_cor_kick.setObjectName("rb_cor_kick")
        self.buttonGroup.addButton(self.rb_cor_kick)
        self.gridLayout_6.addWidget(self.rb_cor_kick, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 2, 0, 1, 2)
        self.gridLayout_11.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.mf_table = OclTable(self.tab)
        self.mf_table.setObjectName("mf_table")
        self.gridLayout_11.addWidget(self.mf_table, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pb_check = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_check.setFont(font)
        self.pb_check.setObjectName("pb_check")
        self.gridLayout_19.addWidget(self.pb_check, 4, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_19.addWidget(self.spinBox, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_19.addWidget(self.label, 3, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_19.addWidget(self.checkBox, 0, 0, 1, 2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_19.addWidget(self.checkBox_2, 1, 0, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_19.addWidget(self.checkBox_3, 2, 0, 1, 2)
        self.gridLayout_18.addLayout(self.gridLayout_19, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 300))
        self.widget.setObjectName("widget")
        self.gridLayout_9.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ocelot Interface"))
        self.pb_read_from_mf.setText(_translate("Form", "Read GO from Current MF"))
        self.groupBox.setTitle(_translate("Form", "Set Min SASE"))
        self.lab_sase_max.setText(_translate("Form", "1000"))
        self.lab_sase_min.setText(_translate("Form", "0"))
        self.lab_sase_cur.setText(_translate("Form", "0"))
        self.lab_nfiles.setText(_translate("Form", "1"))
        self.label_2.setText(_translate("Form", "SASE energy"))
        self.label_3.setText(_translate("Form", "Number of Machine Files"))
        self.pb_find_go_2.setText(_translate("Form", "Get Current State"))
        self.pb_find_go.setText(_translate("Form", "Find GO"))
        self.groupBox_3.setTitle(_translate("Form", "Analysis"))
        self.rb_x_plane.setText(_translate("Form", "X plane"))
        self.rb_yplane.setText(_translate("Form", "Y plane"))
        self.pb_show.setText(_translate("Form", "Show"))
        self.groupBox_2.setTitle(_translate("Form", "Adviser"))
        self.label_8.setText(_translate("Form", "Number of neighbors"))
        self.rb_energy_prof.setText(_translate("Form", "Energy profile"))
        self.rb_cor_kick.setText(_translate("Form", "Correctors Kick"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Adviser"))
        self.groupBox_7.setTitle(_translate("Form", "Parameters"))
        self.pb_check.setText(_translate("Form", "Find"))
        self.label.setText(_translate("Form", "Number of clusters"))
        self.checkBox.setText(_translate("Form", "Correctors Kick"))
        self.checkBox_2.setText(_translate("Form", "BPM X"))
        self.checkBox_3.setText(_translate("Form", "BPM Y"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Clusters"))

from gui.monitors.ocl_monitor import OclMonitor
from gui.tables.ocl_table import OclTable
