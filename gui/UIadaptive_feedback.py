# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIadaptive_feedback.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1152, 781)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #Form.setStyleSheet("background-color: white")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.sb_array_len = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_array_len.setFont(font)
        self.sb_array_len.setMaximum(5000)
        self.sb_array_len.setSingleStep(10)
        self.sb_array_len.setProperty("value", 100)
        self.sb_array_len.setObjectName("sb_array_len")
        self.gridLayout_5.addWidget(self.sb_array_len, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.sb_time_delay = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_time_delay.setFont(font)
        self.sb_time_delay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_time_delay.setMaximum(10.0)
        self.sb_time_delay.setSingleStep(0.01)
        self.sb_time_delay.setProperty("value", 0.1)
        self.sb_time_delay.setObjectName("sb_time_delay")
        self.gridLayout_5.addWidget(self.sb_time_delay, 1, 1, 1, 1)
        self.sb_averaging = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_averaging.setFont(font)
        self.sb_averaging.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_averaging.setMaximum(100.0)
        self.sb_averaging.setSingleStep(10.0)
        self.sb_averaging.setProperty("value", 10.0)
        self.sb_averaging.setObjectName("sb_averaging")
        self.gridLayout_5.addWidget(self.sb_averaging, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.sb_go_recalc_delay = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_go_recalc_delay.setFont(font)
        self.sb_go_recalc_delay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_go_recalc_delay.setMinimum(1.0)
        self.sb_go_recalc_delay.setMaximum(100.0)
        self.sb_go_recalc_delay.setSingleStep(1.0)
        self.sb_go_recalc_delay.setProperty("value", 1.0)
        self.sb_go_recalc_delay.setObjectName("sb_go_recalc_delay")
        self.gridLayout_5.addWidget(self.sb_go_recalc_delay, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 4, 4, 1, 2)
        self.pb_start_feedback = QtWidgets.QPushButton(Form)
        self.pb_start_feedback.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_feedback.setFont(font)
        self.pb_start_feedback.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_feedback.setObjectName("pb_start_feedback")
        self.gridLayout.addWidget(self.pb_start_feedback, 13, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)
        self.pb_start_statistics = QtWidgets.QPushButton(Form)
        self.pb_start_statistics.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_statistics.setFont(font)
        self.pb_start_statistics.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_statistics.setObjectName("pb_start_statistics")
        self.gridLayout.addWidget(self.pb_start_statistics, 13, 4, 1, 2)
        self.sb_feedback_rep = QtWidgets.QDoubleSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_feedback_rep.setFont(font)
        self.sb_feedback_rep.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_feedback_rep.setMinimum(1.0)
        self.sb_feedback_rep.setMaximum(100.0)
        self.sb_feedback_rep.setSingleStep(1.0)
        self.sb_feedback_rep.setProperty("value", 3.0)
        self.sb_feedback_rep.setObjectName("sb_feedback_rep")
        self.gridLayout.addWidget(self.sb_feedback_rep, 13, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 4, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.le_b = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_b.setFont(font)
        self.le_b.setObjectName("le_b")
        self.gridLayout_3.addWidget(self.le_b, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.le_c = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_c.setFont(font)
        self.le_c.setObjectName("le_c")
        self.gridLayout_3.addWidget(self.le_c, 2, 1, 1, 1)
        self.le_a = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_a.setFont(font)
        self.le_a.setObjectName("le_a")
        self.gridLayout_3.addWidget(self.le_a, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.le_of = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_of.setFont(font)
        self.le_of.setObjectName("le_of")
        self.gridLayout_3.addWidget(self.le_of, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(600, 0))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)
        self.sb_afeed_fraction = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_afeed_fraction.setFont(font)
        self.sb_afeed_fraction.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_afeed_fraction.setMaximum(1.0)
        self.sb_afeed_fraction.setSingleStep(0.1)
        self.sb_afeed_fraction.setProperty("value", 0.7)
        self.sb_afeed_fraction.setObjectName("sb_afeed_fraction")
        self.gridLayout_8.addWidget(self.sb_afeed_fraction, 1, 1, 1, 1)
        self.sb_ref_orbit_nread = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_ref_orbit_nread.setFont(font)
        self.sb_ref_orbit_nread.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_ref_orbit_nread.setDecimals(0)
        self.sb_ref_orbit_nread.setMinimum(1.0)
        self.sb_ref_orbit_nread.setMaximum(100.0)
        self.sb_ref_orbit_nread.setSingleStep(1.0)
        self.sb_ref_orbit_nread.setProperty("value", 1.0)
        self.sb_ref_orbit_nread.setObjectName("sb_ref_orbit_nread")
        self.gridLayout_8.addWidget(self.sb_ref_orbit_nread, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 7, 0, 1, 3)
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pb_load_settings = QtWidgets.QPushButton(self.groupBox_5)
        self.pb_load_settings.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_load_settings.setFont(font)
        self.pb_load_settings.setStyleSheet("color: rgb(51, 255, 255);")
        self.pb_load_settings.setObjectName("pb_load_settings")
        self.gridLayout_10.addWidget(self.pb_load_settings, 1, 1, 1, 1)
        self.pb_save_settings = QtWidgets.QPushButton(self.groupBox_5)
        self.pb_save_settings.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_save_settings.setFont(font)
        self.pb_save_settings.setStyleSheet("color: rgb(255, 0, 0);")
        self.pb_save_settings.setObjectName("pb_save_settings")
        self.gridLayout_10.addWidget(self.pb_save_settings, 1, 2, 1, 1)
        self.cb_load_settings = QtWidgets.QComboBox(self.groupBox_5)
        self.cb_load_settings.setObjectName("cb_load_settings")
        self.gridLayout_10.addWidget(self.cb_load_settings, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox_5, 7, 5, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.le_warn = QtWidgets.QLineEdit(self.groupBox_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.le_warn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_warn.setFont(font)
        self.le_warn.setObjectName("le_warn")
        self.gridLayout_9.addWidget(self.le_warn, 1, 1, 1, 1)
        self.cb_update_display = QtWidgets.QCheckBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_update_display.setFont(font)
        self.cb_update_display.setChecked(True)
        self.cb_update_display.setObjectName("cb_update_display")
        self.gridLayout_9.addWidget(self.cb_update_display, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 7, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ocelot Interface"))
        self.groupBox_2.setTitle(_translate("Form", "Statistics Data Control"))
        self.label_3.setText(_translate("Form", "Reading Delay (s)"))
        self.label_2.setText(_translate("Form", "Array Length"))
        self.label_7.setText(_translate("Form", "Averaging Over (%)"))
        self.label_9.setText(_translate("Form", "Recalculate GO (s)"))
        self.pb_start_feedback.setText(_translate("Form", "Start Feedback"))
        self.label_8.setText(_translate("Form", "Apply Feedback Every s  "))
        self.pb_start_statistics.setText(_translate("Form", "Statistics Accum On"))
        self.groupBox.setTitle(_translate("Form", "Objective Function"))
        self.label_6.setText(_translate("Form", "Objective Function   "))
        self.label.setText(_translate("Form", "A:"))
        self.label_4.setText(_translate("Form", "B:"))
        self.label_5.setText(_translate("Form", "C:"))
        self.groupBox_3.setTitle(_translate("Form", "Correction control"))
        self.label_10.setText(_translate("Form", "Apply Fraction"))
        self.label_11.setText(_translate("Form", "Ref Orbit avaraging over last (readings)"))
        self.groupBox_5.setTitle(_translate("Form", "Load Settings"))
        self.pb_load_settings.setText(_translate("Form", "Load"))
        self.pb_save_settings.setText(_translate("Form", "Save"))
        self.groupBox_4.setTitle(_translate("Form", "Indication"))
        self.cb_update_display.setText(_translate("Form", "Update Main Display"))

