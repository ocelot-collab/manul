#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:00:50 2017

@author: S.Tomin and D.Lipka 
"""
import pydoocs as pyd
import os
from PyQt5 import QtGui

BPM_LOCATION_FILE = "BPMDAMC02_locations_201802.txt"

class BPMDoocsInterface:
    def __init__(self, ui_textbox=None):
        self.textbox = ui_textbox

    
    def read_doocs_values(self, addresses, doocs_property):
        results = []
        for address in addresses:
            address_single = address + doocs_property
            #print(address_single)
            try:
                results += [pyd.read(address_single)['data']]
            except:
                message = "Following address does not get a doocs value"
                message += address_single 
                if self.textbox != None:
                    self.textbox.setTextColor(QtGui.QColor(255, 0, 0))
                    self.textbox.append(message)
                    self.textbox.setTextColor(QtGui.QColor(0, 0, 0))
                else:
                    print(message)
        return results 

    def write_doocs_values(self, addresses, doocs_property, value):

        for address in addresses:
            address_single = address + doocs_property
            #print(address_single)
            try:
                pyd.write(address_single,value)
            except:
                message = "Following address does not allow to set a doocs value"
                message += address_single 
                if self.textbox != None:
                    self.textbox.setTextColor(QtGui.QColor(255, 0, 0))
                    self.textbox.append(message)
                    self.textbox.setTextColor(QtGui.QColor(0, 0, 0))
                else:
                    print(message)

    def write_doocs_array(self,addresses,doocs_property,value):
        i = 0
        for address in addresses:
            address_single = address + doocs_property
            #print(address_single)
            try:
                pyd.write(address_single,value[i])
                i = i + 1
            except:
                message = "Following address does not allow to set a doocs value"
                message += address_single 
                if self.textbox != None:
                    self.textbox.setTextColor(QtGui.QColor(255, 0, 0))
                    self.textbox.append(message)
                    self.textbox.setTextColor(QtGui.QColor(0, 0, 0))
                else:
                    print(message)


class ButtonBPM:
    """
    API for button BPM
    
    mi - machine interface 
    BPM_addresses - Cavity BPM addresses
    """
    
    def __init__(self, mi=None):
        if mi == None:
            self.mi = BPMDoocsInterface()
        # "BPMDAMC02_locations.txt"
        path = os.path.realpath(__name__)
        indx = path.find("bpm_api")
        self.filename = path[:indx] +"bpm_api" + os.sep + BPM_LOCATION_FILE
        self.bpm_addresses = self.get_BPM_addresses_from_file()

    def activate(self, max_charge_value, max_pos_value):
        """
        Method to activate "freeze" mode of button BPMs
        
        max_charge_value - in [pC]
        max_pos_value - in [mm]
        """
        print("Button activate")
        self.mi.write_doocs_values(self.bpm_addresses,'/AUTO_GAIN_CTRL_MA_C',max_charge_value)
        
        self.mi.write_doocs_values(self.bpm_addresses,'/AUTO_GAIN_CTRL_MA_P',max_pos_value)
        
        self.mi.write_doocs_values(self.bpm_addresses,'/AUTO_GAIN_CTRL_MODE',1)

    def deactivate(self):
        """
        Method to deactivate "freeze" mode of  button BPMs
        
        """
        
        print("Deactivate Button BPM Amplitude Mode")
        
        self.mi.write_doocs_values(self.bpm_addresses,'/AUTO_GAIN_CTRL_MA_C',1010)
        self.mi.write_doocs_values(self.bpm_addresses,'/AUTO_GAIN_CTRL_MA_P',2.0)
        self.mi.write_doocs_values(self.bpm_addresses,'/AUTO_GAIN_CTRL_MODE',0)

    def get_BPM_addresses_from_file(self):
        address = []
        address_start = "XFEL.DIAG/BPMDAMC2/"
        #addresses = ["DI30I1.1_GPAC.1_BPMG.24I.I1","DI30I1.1_GPAC.1_BPMG.25I.I1","DI30I1.1_GPAC.1_BPMG.25II.I1"]



        name_all_locations = [line.rstrip('\n') for line in open(self.filename)]
        #print(name_all_locations)
        addresses = []
        for address_single in name_all_locations:
            #print(address_single)
            if address_single.find("BPMG") > 0:
                addresses += [address_single]
            if address_single.find("BPMA") > 0:
                addresses += [address_single]
            if address_single.find("BPMC") > 0:
                addresses += [address_single]
            if address_single.find("BPMD") > 0:
                addresses += [address_single]
            if address_single.find("BPMW") > 0:
                addresses += [address_single]
        #print(test_addresses)
        
        for address_single in addresses:
            address += [address_start + address_single]

        return address



class CavityBPM:
    """
    API for cavity BPM
    
    mi - machine interface 
    BPM_addresses - Cavity BPM addresses
    """
    
    def __init__(self, mi=None):
        if mi == None:
            self.mi = BPMDoocsInterface()
        path = os.path.realpath(__name__)
        indx = path.find("bpm_api")
        self.filename = path[:indx] +"bpm_api" + os.sep + BPM_LOCATION_FILE
        self.bpm_addresses = self.get_BPM_addresses_from_file()
        
    def activate(self, attenuation):
        """
        Method to activate "freeze" mode of cavity BPMs
        
        attenuation - in [db]
        """
        print("Cavity activate")
        attenuator_setting_Q = self.mi.read_doocs_values(self.bpm_addresses,'/R_DSA')

        attenuator_setting_X = self.mi.read_doocs_values(self.bpm_addresses,'/X_DSA')

        attenuator_setting_Y = self.mi.read_doocs_values(self.bpm_addresses,'/Y_DSA')

        for i in range(0,len(attenuator_setting_Q)):
            #attenuator_setting_Q[i] = attenuator_setting_Q[i] + attenuation*2
            attenuator_setting_Q[i] = 20 + attenuation*2
        
        for i in range(0,len(attenuator_setting_X)):
            #attenuator_setting_X[i] = attenuator_setting_X[i] + attenuation*2
            attenuator_setting_X[i] = 0 + attenuation*2

        for i in range(0,len(attenuator_setting_Y)):
            #attenuator_setting_Y[i] = attenuator_setting_Y[i] + attenuation*2
            attenuator_setting_Y[i] = 0 + attenuation*2


        self.mi.write_doocs_values(self.bpm_addresses,'/REF_GAIN_FB_ON',0)
        self.mi.write_doocs_values(self.bpm_addresses,'/X_GAIN_FB_ON',0)
        self.mi.write_doocs_values(self.bpm_addresses,'/Y_GAIN_FB_ON',0)
        
        self.mi.write_doocs_array(self.bpm_addresses,'/R_DSA',attenuator_setting_Q)
        self.mi.write_doocs_array(self.bpm_addresses,'/X_DSA',attenuator_setting_X)
        self.mi.write_doocs_array(self.bpm_addresses,'/Y_DSA',attenuator_setting_Y)
        
    def deactivate(self):
        """
        Method to deactivate "freeze" mode of the cavity BPMs
        
        """
        print("AGC on")
        self.mi.write_doocs_values(self.bpm_addresses,'/REF_GAIN_FB_ON',1)
        self.mi.write_doocs_values(self.bpm_addresses,'/X_GAIN_FB_ON',1)
        self.mi.write_doocs_values(self.bpm_addresses,'/Y_GAIN_FB_ON',1)


    def get_BPM_addresses_from_file(self):
        address = []
        address_start = "XFEL.DIAG/BPMDAMC2/"



        name_all_locations = [line.rstrip('\n') for line in open(self.filename)]
        #print(name_all_locations)
        addresses = []
        for address_single in name_all_locations:
            #print(address_single)
            if address_single.find("BPME") > 0:
                addresses += [address_single]
            if address_single.find("BPMF") > 0:
                addresses += [address_single]
            if address_single.find("BPMI") > 0:
                addresses += [address_single]
        #print(test_addresses)

        for address_single in addresses:
            address += [address_start + address_single]

        return address