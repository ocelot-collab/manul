"""
Settings. S.Tomin.
"""

import sys
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QMessageBox, QApplication,QMenu, QWidget, QAction, QTableWidget, QTableWidgetItem, QDoubleSpinBox
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from gui.UISettings import Ui_Form
import json
#import logging
#logger = logging.getLogger(__name__)

class ManulSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        #QWidget.__init__(self, parent)
        self.master = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.setStyleSheet("background-color:black;")
        #self.ui.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.ui.pb_apply.clicked.connect(self.apply_settings)
        self.ui.cb_single_shot.stateChanged.connect(self.single_shot_set)

        self.ui.cb_charge_doocs.stateChanged.connect(self.read_charge_from_doocs)

        self.ui.pb_cancel.clicked.connect(self.close)
        self.ui.cb_style_def.addItem("standard.css")
        self.ui.cb_style_def.addItem("colinDark.css")
        self.ui.cb_style_def.addItem("dark.css")
        self.load_state(filename=self.master.config_file)
        self.loadStyleSheet(filename=self.style_file)


    def read_charge_from_doocs(self):
        if self.ui.cb_charge_doocs.isChecked():
            self.ui.sb_bunch_charge.setEnabled(False)
            self.ui.label_17.setEnabled(False)
        else:
            self.ui.sb_bunch_charge.setEnabled(True)
            self.ui.label_17.setEnabled(True)

    def single_shot_set(self):
        if self.ui.cb_single_shot.isChecked():
            self.ui.sb_nreadings.setEnabled(False)
            self.ui.sb_nlast.setEnabled(False)
            self.ui.label_2.setEnabled(False)
            self.ui.label_8.setEnabled(False)
        else:
            self.ui.sb_nreadings.setEnabled(True)
            self.ui.sb_nlast.setEnabled(True)
            self.ui.label_2.setEnabled(True)
            self.ui.label_8.setEnabled(True)

    def apply_settings(self):
        update = self.question_box("Save Settings and Close?")
        if update:
            if not os.path.exists(self.master.config_dir):
                os.makedirs(self.master.config_dir)
            self.save_state(self.master.config_file)
            self.master.load_settings()
            self.close()

    def save_state(self, filename):
        table = {}
        table["show_correction_result"] = self.ui.cb_show_correction_result.checkState()
        table["nlast"] = self.ui.sb_nlast.value()
        table["nreadings"] = self.ui.sb_nreadings.value()
        table["lattice"] = self.ui.le_lattice.text()
        table["logbook"] = self.ui.le_logbook.text()
        table["epsilon_x"] = self.ui.sb_epsilon_x.value()
        table["epsilon_y"] = self.ui.sb_epsilon_y.value()
        table["uncheck_corrs"] = self.string2list(self.ui.te_corrs.toPlainText())
        table["uncheck_bpms"] = self.string2list(self.ui.te_bpms.toPlainText())
        table["single_shot"] = self.ui.cb_single_shot.checkState()

        table["le_cl_energy"] = self.ui.le_cl_energy.text()
        table["le_b2_energy"] = self.ui.le_b2_energy.text()
        table["le_b1_energy"] = self.ui.le_b1_energy.text()
        table["le_i1_energy"] = self.ui.le_i1_energy.text()

        table["co_nlast"] = self.ui.sb_co_nlast.value()

        table["server_list"] = self.string2list(self.ui.le_server.text())
        table["server"] = self.ui.combo_server.currentText()

        table["bpm_server_list"] = self.string2list(self.ui.le_bpm_server.text())
        table["bpm_server"] = self.ui.combo_bpm_server.currentText()

        table["subtrain_list"] = self.string2list(self.ui.le_subtrain.text())
        table["subtrain"] = self.ui.combo_subtrain.currentText()

        table["charge_tol"] = self.ui.sb_charge_tol.value()
        table["bunch_charge"] = self.ui.sb_bunch_charge.value()
        table["charge_doocs"] = self.ui.cb_charge_doocs.checkState()

        table["show_cor_panel"] = self.ui.cb_show_cor_panel.checkState()
        table["style"] = self.ui.cb_style_def.currentIndex()
        table["style_file"] = self.ui.cb_style_def.currentText()

        table["beta"] = self.ui.sb_beta.value()

        with open(filename, 'w') as f:
            json.dump(table, f)
        print("SAVE State")

    def list2string(self, dev_list):
        return ", ".join(dev_list)
    
    def string2list(self, dev_str):
        lst = dev_str.split(",")
        lst = [text.replace(" ", "") for text in lst]
        lst = [text.replace("\n", "") for text in lst]
        return lst

    def load_state(self, filename):
        # pvs = self.ui.widget.pvs
        with open(filename, 'r') as f:
            table = json.load(f)

        self.ui.cb_show_correction_result.setCheckState(table["show_correction_result"])
        self.ui.sb_nlast.setValue(table["nlast"])
        self.ui.sb_nreadings.setValue(table["nreadings"])
        self.ui.le_lattice.setText(table["lattice"])
        if "logbook" in table.keys():  self.ui.le_logbook.setText(table["logbook"])

        if "epsilon_x" in table.keys():  self.ui.sb_epsilon_x.setValue(table["epsilon_x"])
        if "epsilon_y" in table.keys():  self.ui.sb_epsilon_y.setValue(table["epsilon_y"])
        if "uncheck_corrs" in table.keys(): self.ui.te_corrs.setPlainText(self.list2string(table["uncheck_corrs"]))
        if "uncheck_bpms" in table.keys():  self.ui.te_bpms.setPlainText(self.list2string(table["uncheck_bpms"]))
        if "single_shot" in table.keys(): self.ui.cb_single_shot.setCheckState(table["single_shot"])

        if "le_cl_energy" in table.keys(): self.ui.le_cl_energy.setText(table["le_cl_energy"])
        if "le_b2_energy" in table.keys(): self.ui.le_b2_energy.setText(table["le_b2_energy"])
        if "le_b1_energy" in table.keys(): self.ui.le_b1_energy.setText(table["le_b1_energy"])
        if "le_i1_energy" in table.keys(): self.ui.le_i1_energy.setText(table["le_i1_energy"])

        if "co_nlast" in table.keys(): self.ui.sb_co_nlast.setValue(table["co_nlast"])

        if "server_list" in table.keys():
            self.ui.le_server.setText(self.list2string(table["server_list"]))
            for name in table["server_list"]:
                self.ui.combo_server.addItem(name)
            if "server" in table.keys() and table["server"] in table["server_list"]:
                indx = table["server_list"].index(table["server"])
            else:
                indx = 0
            self.ui.combo_server.setCurrentIndex(indx)

        if "bpm_server_list" in table.keys():
            self.ui.le_bpm_server.setText(self.list2string(table["bpm_server_list"]))
            for name in table["bpm_server_list"]:
                self.ui.combo_bpm_server.addItem(name)
            if "bpm_server" in table.keys() and table["bpm_server"] in table["bpm_server_list"]:
                indx = table["bpm_server_list"].index(table["bpm_server"])
            else:
                indx = 0
            self.ui.combo_bpm_server.setCurrentIndex(indx)

        if "subtrain_list" in table.keys():
            self.ui.le_subtrain.setText(self.list2string(table["subtrain_list"]))
            for name in table["subtrain_list"]:
                self.ui.combo_subtrain.addItem(name)

            if "subtrain" in table.keys() and table["subtrain"] in table["subtrain_list"]:
                indx = table["subtrain_list"].index(table["subtrain"])
            else:
                indx = 0

            self.ui.combo_subtrain.setCurrentIndex(indx)

        if "charge_tol" in table.keys(): self.ui.sb_charge_tol.setValue(table["charge_tol"])
        if "bunch_charge" in table.keys(): self.ui.sb_bunch_charge.setValue(table["bunch_charge"])
        if "charge_doocs" in table.keys(): self.ui.cb_charge_doocs.setCheckState(table["charge_doocs"])

        if "show_cor_panel" in table.keys(): self.ui.cb_show_cor_panel.setCheckState(table["show_cor_panel"])
        if "style" in table.keys(): self.ui.cb_style_def.setCurrentIndex(table["style"])
        self.style_file = self.ui.cb_style_def.currentText()

        if "beta" in table.keys(): self.ui.sb_beta.setValue(table["beta"])
        #if "cb_lattice" in table.keys(): self.ui.sb_co_nlast.setValue(table["co_nlast"])

#        a = table["uncheck_corrs"].split(",")
#        a = [text.replace(" ", "") for text in a]
#        a = [text.replace("\n", "") for text in a]
#        print(a)
        print("LOAD State")

    #def save_presettings(self):
    #    update = self.question_box("Rewrite Settings ?")
    #    if update:
    #        if not os.path.exists(self.master.configs_dir):
    #            os.makedirs(self.master.configs_dir)
    #        self.save_state(self.master.configs_dir + "settings.json")
    #        self.parent.load_settings()


    def question_box(self, message):
        #QtGui.QMessageBox.question(self, "Question box", message)
        reply = QMessageBox.question(self, "Question Box",
                message,
                QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True

        return False

    def loadStyleSheet(self, filename):
        """ Load in the dark theme style sheet. """
        try:
            self.cssfile = self.master.gui_dir + filename
            print(self.cssfile)
            with open(self.cssfile, "r") as f:
                #print(f)
                self.setStyleSheet(f.read())
        except IOError:
            print('No style sheet found!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ManulSettings()
    window.show()
    sys.exit(app.exec_())