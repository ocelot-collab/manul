# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UImanul.ui'
#
# Created: Thu Apr 13 10:59:46 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1200, 1049)
        Form.setMinimumSize(QtCore.QSize(1150, 0))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Form.setStyleSheet(_fromUtf8("background-color: white"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.groupBox_9 = QtGui.QGroupBox(Form)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_15 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.cb_sec_order = QtGui.QCheckBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_sec_order.setFont(font)
        self.cb_sec_order.setObjectName(_fromUtf8("cb_sec_order"))
        self.gridLayout_14.addWidget(self.cb_sec_order, 0, 0, 1, 1)
        self.cb_coupler_kick = QtGui.QCheckBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_coupler_kick.setFont(font)
        self.cb_coupler_kick.setObjectName(_fromUtf8("cb_coupler_kick"))
        self.gridLayout_14.addWidget(self.cb_coupler_kick, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_9)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.cb_lattice = QtGui.QComboBox(self.groupBox_3)
        self.cb_lattice.setMinimumSize(QtCore.QSize(0, 43))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_lattice.setFont(font)
        self.cb_lattice.setObjectName(_fromUtf8("cb_lattice"))
        self.gridLayout_4.addWidget(self.cb_lattice, 1, 0, 1, 1)
        self.pb_reload = QtGui.QPushButton(self.groupBox_3)
        self.pb_reload.setMinimumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_reload.setFont(font)
        self.pb_reload.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_reload.setObjectName(_fromUtf8("pb_reload"))
        self.gridLayout_4.addWidget(self.pb_reload, 1, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.widget_2 = QtGui.QWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(700, 400))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_6.addWidget(self.widget_2, 0, 0, 1, 2)
        self.widget = QtGui.QWidget(self.tab_2)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(400, 200))
        self.widget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_6.addWidget(self.widget, 0, 2, 1, 2)
        self.groupBox_10 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cb_otr55 = QtGui.QCheckBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_otr55.setFont(font)
        self.cb_otr55.setChecked(True)
        self.cb_otr55.setObjectName(_fromUtf8("cb_otr55"))
        self.verticalLayout.addWidget(self.cb_otr55)
        self.cb_otr218 = QtGui.QCheckBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_otr218.setFont(font)
        self.cb_otr218.setObjectName(_fromUtf8("cb_otr218"))
        self.verticalLayout.addWidget(self.cb_otr218)
        self.cb_otr450 = QtGui.QCheckBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_otr450.setFont(font)
        self.cb_otr450.setObjectName(_fromUtf8("cb_otr450"))
        self.verticalLayout.addWidget(self.cb_otr450)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_6.addWidget(self.groupBox_10, 1, 0, 1, 4)
        self.pb_write = QtGui.QPushButton(self.tab_2)
        self.pb_write.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_write.setFont(font)
        self.pb_write.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_write.setObjectName(_fromUtf8("pb_write"))
        self.gridLayout_6.addWidget(self.pb_write, 2, 0, 2, 1)
        self.pb_read = QtGui.QPushButton(self.tab_2)
        self.pb_read.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_read.setFont(font)
        self.pb_read.setStyleSheet(_fromUtf8("color: rgb(85, 255, 255);"))
        self.pb_read.setObjectName(_fromUtf8("pb_read"))
        self.gridLayout_6.addWidget(self.pb_read, 2, 1, 2, 1)
        self.pb_reset = QtGui.QPushButton(self.tab_2)
        self.pb_reset.setEnabled(True)
        self.pb_reset.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_reset.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_reset.setFont(font)
        self.pb_reset.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_reset.setObjectName(_fromUtf8("pb_reset"))
        self.gridLayout_6.addWidget(self.pb_reset, 2, 2, 1, 2)
        self.pb_update = QtGui.QPushButton(self.tab_2)
        self.pb_update.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_update.setFont(font)
        self.pb_update.setObjectName(_fromUtf8("pb_update"))
        self.gridLayout_6.addWidget(self.pb_update, 3, 2, 1, 2)
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.w_orbit = QtGui.QWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_orbit.sizePolicy().hasHeightForWidth())
        self.w_orbit.setSizePolicy(sizePolicy)
        self.w_orbit.setMinimumSize(QtCore.QSize(650, 400))
        self.w_orbit.setObjectName(_fromUtf8("w_orbit"))
        self.horizontalLayout_4.addWidget(self.w_orbit)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb_apply_kicks = QtGui.QPushButton(self.tab_3)
        self.pb_apply_kicks.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_apply_kicks.setFont(font)
        self.pb_apply_kicks.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_apply_kicks.setObjectName(_fromUtf8("pb_apply_kicks"))
        self.horizontalLayout_2.addWidget(self.pb_apply_kicks)
        self.pb_correct_orbit = QtGui.QPushButton(self.tab_3)
        self.pb_correct_orbit.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_correct_orbit.setFont(font)
        self.pb_correct_orbit.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_correct_orbit.setObjectName(_fromUtf8("pb_correct_orbit"))
        self.horizontalLayout_2.addWidget(self.pb_correct_orbit)
        self.frame_3 = QtGui.QFrame(self.tab_3)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pb_update_3 = QtGui.QPushButton(self.frame_3)
        self.pb_update_3.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_update_3.setFont(font)
        self.pb_update_3.setObjectName(_fromUtf8("pb_update_3"))
        self.verticalLayout_4.addWidget(self.pb_update_3)
        self.pb_update_4 = QtGui.QPushButton(self.frame_3)
        self.pb_update_4.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_update_4.setFont(font)
        self.pb_update_4.setObjectName(_fromUtf8("pb_update_4"))
        self.verticalLayout_4.addWidget(self.pb_update_4)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pb_disp_meas = QtGui.QPushButton(self.groupBox_2)
        self.pb_disp_meas.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_disp_meas.setFont(font)
        self.pb_disp_meas.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_disp_meas.setObjectName(_fromUtf8("pb_disp_meas"))
        self.verticalLayout_3.addWidget(self.pb_disp_meas)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.sb_dV = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sb_dV.setFont(font)
        self.sb_dV.setMinimum(-5.0)
        self.sb_dV.setMaximum(5.0)
        self.sb_dV.setSingleStep(0.1)
        self.sb_dV.setProperty("value", 2.0)
        self.sb_dV.setObjectName(_fromUtf8("sb_dV"))
        self.horizontalLayout_5.addWidget(self.sb_dV)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 3, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pb_read_orbit = QtGui.QPushButton(self.groupBox_2)
        self.pb_read_orbit.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_read_orbit.setFont(font)
        self.pb_read_orbit.setStyleSheet(_fromUtf8("color: rgb(85, 255, 255);"))
        self.pb_read_orbit.setObjectName(_fromUtf8("pb_read_orbit"))
        self.verticalLayout_6.addWidget(self.pb_read_orbit)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.sb_alpha = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sb_alpha.setFont(font)
        self.sb_alpha.setMinimum(0.0)
        self.sb_alpha.setMaximum(1.0)
        self.sb_alpha.setSingleStep(0.1)
        self.sb_alpha.setProperty("value", 0.0)
        self.sb_alpha.setObjectName(_fromUtf8("sb_alpha"))
        self.horizontalLayout_6.addWidget(self.sb_alpha)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 2, 2, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.pb_calc_RM = QtGui.QPushButton(self.groupBox_2)
        self.pb_calc_RM.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_calc_RM.setFont(font)
        self.pb_calc_RM.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_calc_RM.setObjectName(_fromUtf8("pb_calc_RM"))
        self.verticalLayout_7.addWidget(self.pb_calc_RM)
        self.pb_calc_misal = QtGui.QPushButton(self.groupBox_2)
        self.pb_calc_misal.setEnabled(True)
        self.pb_calc_misal.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_calc_misal.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_calc_misal.setFont(font)
        self.pb_calc_misal.setStyleSheet(_fromUtf8("color: rgb(85, 255, 255);"))
        self.pb_calc_misal.setObjectName(_fromUtf8("pb_calc_misal"))
        self.verticalLayout_7.addWidget(self.pb_calc_misal)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_11.addWidget(self.label)
        self.sb_kick_weight = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sb_kick_weight.setFont(font)
        self.sb_kick_weight.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_kick_weight.setMinimum(0.0)
        self.sb_kick_weight.setMaximum(1.0)
        self.sb_kick_weight.setSingleStep(0.05)
        self.sb_kick_weight.setProperty("value", 1.0)
        self.sb_kick_weight.setObjectName(_fromUtf8("sb_kick_weight"))
        self.horizontalLayout_11.addWidget(self.sb_kick_weight)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.cb_online_orbit = QtGui.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_online_orbit.setFont(font)
        self.cb_online_orbit.setObjectName(_fromUtf8("cb_online_orbit"))
        self.verticalLayout_8.addWidget(self.cb_online_orbit)
        self.gridLayout_3.addLayout(self.verticalLayout_8, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 4, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(self.tab_3)
        self.tabWidget.setMaximumSize(QtCore.QSize(420, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.w_cor = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_cor.sizePolicy().hasHeightForWidth())
        self.w_cor.setSizePolicy(sizePolicy)
        self.w_cor.setMinimumSize(QtCore.QSize(450, 121))
        self.w_cor.setMaximumSize(QtCore.QSize(400, 16777215))
        self.w_cor.setObjectName(_fromUtf8("w_cor"))
        self.gridLayout_2.addWidget(self.w_cor, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_reset_all = QtGui.QPushButton(self.tab)
        self.pb_reset_all.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_reset_all.setFont(font)
        self.pb_reset_all.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_reset_all.setObjectName(_fromUtf8("pb_reset_all"))
        self.horizontalLayout.addWidget(self.pb_reset_all)
        self.pb_check = QtGui.QPushButton(self.tab)
        self.pb_check.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_check.setFont(font)
        self.pb_check.setObjectName(_fromUtf8("pb_check"))
        self.horizontalLayout.addWidget(self.pb_check)
        self.pb_uncheck = QtGui.QPushButton(self.tab)
        self.pb_uncheck.setEnabled(True)
        self.pb_uncheck.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_uncheck.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_uncheck.setFont(font)
        self.pb_uncheck.setStyleSheet(_fromUtf8(""))
        self.pb_uncheck.setObjectName(_fromUtf8("pb_uncheck"))
        self.horizontalLayout.addWidget(self.pb_uncheck)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.cb_x_cors = QtGui.QCheckBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_x_cors.setFont(font)
        self.cb_x_cors.setObjectName(_fromUtf8("cb_x_cors"))
        self.horizontalLayout_10.addWidget(self.cb_x_cors)
        self.cb_y_cors = QtGui.QCheckBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_y_cors.setFont(font)
        self.cb_y_cors.setObjectName(_fromUtf8("cb_y_cors"))
        self.horizontalLayout_10.addWidget(self.cb_y_cors)
        self.pb_uncheck_red = QtGui.QPushButton(self.tab)
        self.pb_uncheck_red.setEnabled(True)
        self.pb_uncheck_red.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_uncheck_red.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_uncheck_red.setFont(font)
        self.pb_uncheck_red.setStyleSheet(_fromUtf8(""))
        self.pb_uncheck_red.setObjectName(_fromUtf8("pb_uncheck_red"))
        self.horizontalLayout_10.addWidget(self.pb_uncheck_red)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.w_bpm = QtGui.QWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_bpm.sizePolicy().hasHeightForWidth())
        self.w_bpm.setSizePolicy(sizePolicy)
        self.w_bpm.setMinimumSize(QtCore.QSize(400, 300))
        self.w_bpm.setObjectName(_fromUtf8("w_bpm"))
        self.gridLayout_7.addWidget(self.w_bpm, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pb_bpm_check = QtGui.QPushButton(self.tab_4)
        self.pb_bpm_check.setObjectName(_fromUtf8("pb_bpm_check"))
        self.horizontalLayout_3.addWidget(self.pb_bpm_check)
        self.pb_bpm_uncheck = QtGui.QPushButton(self.tab_4)
        self.pb_bpm_uncheck.setObjectName(_fromUtf8("pb_bpm_uncheck"))
        self.horizontalLayout_3.addWidget(self.pb_bpm_uncheck)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout_8.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ocelot Interface", None))
        self.groupBox_9.setTitle(_translate("Form", "Calc Options", None))
        self.cb_sec_order.setText(_translate("Form", "Second Order", None))
        self.cb_coupler_kick.setText(_translate("Form", "Coupler Kick", None))
        self.groupBox_3.setTitle(_translate("Form", "Lattice", None))
        self.pb_reload.setText(_translate("Form", "Reload Lattice", None))
        self.groupBox_10.setTitle(_translate("Form", "BackTracking", None))
        self.cb_otr55.setText(_translate("Form", "OTRC 55", None))
        self.cb_otr218.setText(_translate("Form", "OTRB 218", None))
        self.cb_otr450.setText(_translate("Form", "OTRB 450", None))
        self.pb_write.setText(_translate("Form", "Write to Quads", None))
        self.pb_read.setText(_translate("Form", "Read from Quads", None))
        self.pb_reset.setText(_translate("Form", "Reset All", None))
        self.pb_update.setText(_translate("Form", "Update Reference", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "Twiss", None))
        self.pb_apply_kicks.setText(_translate("Form", "Apply Kicks", None))
        self.pb_correct_orbit.setText(_translate("Form", "Correct Orbit/Dispersion", None))
        self.pb_update_3.setText(_translate("Form", "Update Reference", None))
        self.pb_update_4.setText(_translate("Form", "Save Orbit as Ref", None))
        self.groupBox_2.setTitle(_translate("Form", "Controls", None))
        self.pb_disp_meas.setText(_translate("Form", "Measure Dispersion", None))
        self.label_2.setText(_translate("Form", "dV [MV]", None))
        self.pb_read_orbit.setText(_translate("Form", "Read BPMs/Correctors", None))
        self.label_3.setText(_translate("Form", "alpha (0-orbit. 1-disp)", None))
        self.pb_calc_RM.setText(_translate("Form", "Calculate RM", None))
        self.pb_calc_misal.setText(_translate("Form", "Calculate Misalignment", None))
        self.label.setText(_translate("Form", "Kicks Weight ", None))
        self.cb_online_orbit.setText(_translate("Form", "Online Orbit", None))
        self.pb_reset_all.setText(_translate("Form", "Reset All", None))
        self.pb_check.setText(_translate("Form", "Check", None))
        self.pb_uncheck.setText(_translate("Form", "Uncheck", None))
        self.cb_x_cors.setText(_translate("Form", "X", None))
        self.cb_y_cors.setText(_translate("Form", "Y", None))
        self.pb_uncheck_red.setText(_translate("Form", "Uncheck Red", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Correctors", None))
        self.pb_bpm_check.setText(_translate("Form", "Check", None))
        self.pb_bpm_uncheck.setText(_translate("Form", "Uncheck", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "BPMs", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "Orbit", None))

