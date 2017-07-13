# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIadaptive_feedback.ui'
#
# Created: Wed Jul 12 14:56:49 2017
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
        Form.resize(1152, 781)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Form.setStyleSheet(_fromUtf8("background-color: white"))
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout.addWidget(self.widget_2, 0, 3, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.sb_array_len = QtGui.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_array_len.setFont(font)
        self.sb_array_len.setMaximum(5000)
        self.sb_array_len.setSingleStep(10)
        self.sb_array_len.setProperty("value", 100)
        self.sb_array_len.setObjectName(_fromUtf8("sb_array_len"))
        self.gridLayout_5.addWidget(self.sb_array_len, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.sb_time_delay = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_time_delay.setFont(font)
        self.sb_time_delay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_time_delay.setMaximum(10.0)
        self.sb_time_delay.setSingleStep(0.01)
        self.sb_time_delay.setProperty("value", 0.1)
        self.sb_time_delay.setObjectName(_fromUtf8("sb_time_delay"))
        self.gridLayout_5.addWidget(self.sb_time_delay, 1, 1, 1, 1)
        self.sb_averaging = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_averaging.setFont(font)
        self.sb_averaging.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_averaging.setMaximum(100.0)
        self.sb_averaging.setSingleStep(10.0)
        self.sb_averaging.setProperty("value", 10.0)
        self.sb_averaging.setObjectName(_fromUtf8("sb_averaging"))
        self.gridLayout_5.addWidget(self.sb_averaging, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 4, 3, 1, 1)
        self.sb_feedback_rep = QtGui.QDoubleSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_feedback_rep.setFont(font)
        self.sb_feedback_rep.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_feedback_rep.setMinimum(1.0)
        self.sb_feedback_rep.setMaximum(100.0)
        self.sb_feedback_rep.setSingleStep(1.0)
        self.sb_feedback_rep.setProperty("value", 1.0)
        self.sb_feedback_rep.setObjectName(_fromUtf8("sb_feedback_rep"))
        self.gridLayout.addWidget(self.sb_feedback_rep, 9, 1, 1, 1)
        self.pb_start_statistics = QtGui.QPushButton(Form)
        self.pb_start_statistics.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_statistics.setFont(font)
        self.pb_start_statistics.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_start_statistics.setObjectName(_fromUtf8("pb_start_statistics"))
        self.gridLayout.addWidget(self.pb_start_statistics, 9, 3, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.pb_start_feedback = QtGui.QPushButton(Form)
        self.pb_start_feedback.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_feedback.setFont(font)
        self.pb_start_feedback.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_start_feedback.setObjectName(_fromUtf8("pb_start_feedback"))
        self.gridLayout.addWidget(self.pb_start_feedback, 9, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.le_b = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_b.setFont(font)
        self.le_b.setObjectName(_fromUtf8("le_b"))
        self.gridLayout_3.addWidget(self.le_b, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.le_c = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_c.setFont(font)
        self.le_c.setObjectName(_fromUtf8("le_c"))
        self.gridLayout_3.addWidget(self.le_c, 2, 1, 1, 1)
        self.le_a = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_a.setFont(font)
        self.le_a.setObjectName(_fromUtf8("le_a"))
        self.gridLayout_3.addWidget(self.le_a, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.le_of = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_of.setFont(font)
        self.le_of.setObjectName(_fromUtf8("le_of"))
        self.gridLayout_3.addWidget(self.le_of, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(600, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ocelot Interface", None))
        self.groupBox_2.setTitle(_translate("Form", "Statistics Data Control", None))
        self.label_3.setText(_translate("Form", "Time Delay", None))
        self.label_2.setText(_translate("Form", "Array Length", None))
        self.label_7.setText(_translate("Form", "Averaging over (%)", None))
        self.pb_start_statistics.setText(_translate("Form", "Statistics Accum On", None))
        self.label_8.setText(_translate("Form", "Apply Feedback Every s  ", None))
        self.pb_start_feedback.setText(_translate("Form", "Start Feedback", None))
        self.groupBox.setTitle(_translate("Form", "Objective Function", None))
        self.label_6.setText(_translate("Form", "Objective Function   ", None))
        self.label.setText(_translate("Form", "A:", None))
        self.label_4.setText(_translate("Form", "B:", None))
        self.label_5.setText(_translate("Form", "C:", None))
