"""
XFEL machine interface
S.Tomin, 2017
"""
from __future__ import absolute_import, print_function

try:
    # in server "doocsdev12" set environment
    #  $ export PYTHONPATH=/home/ttflinac/user/python-2.7/Debian/
    import epics
except:
    pass  # Show message on Constructor if we try to use it.

import sys
import numpy as np
import subprocess
import base64
from threading import Lock
from mint.interface import MachineInterface, Device
import mint.bessy_devices as devices
import logging
from lattices import ring_lattice_manager as lattice_manager
logger = logging.getLogger(__name__)
from ocelot.cpbd.response_matrix import *
        
class CorrectorData():

    def __init__(self):
        pass

    def connect(self, corr_names):
        self.ch = []

        corrs = {}
        for b in corr_names:
            self.ch.append( epics.ca.create_channel(b+":rdbk", auto_cb=False) )
            epics.ca.connect_channel(self.ch[-1])


        epics.ca.poll()
    
    def get(self):
        self.corrs = {}

        for c in self.ch:
            epics.ca.get(c, wait=False)

        epics.ca.poll()
        o = {}

        for c in self.ch:
            name = epics.ca.name(c).replace(":rdbk","")
            x = epics.ca.get_complete(c)
            o[name] = x
            
        return o



class OrbitData():

    def __init__(self):
        pass

    def connect(self, bpms_names):
        self.ch_x = []
        self.ch_y = []
        self.offsets = {}

        orb = {}
        for b in bpms_names:
            self.ch_x.append( epics.ca.create_channel(b+":rdX", auto_cb=False) )
            self.ch_y.append( epics.ca.create_channel(b+":rdY", auto_cb=False) )
            epics.ca.connect_channel(self.ch_x[-1])
            epics.ca.connect_channel(self.ch_y[-1])
            xoff = epics.PV(b+":rdX.EOFF").get()
            yoff = epics.PV(b+":rdY.EOFF").get()
            self.offsets[b] = (xoff, yoff)


        epics.ca.poll()
    
    def get(self):
        self.orb = {}
        for c in self.ch_x:
            epics.ca.get(c, wait=False)
        for c in self.ch_y:
            epics.ca.get(c, wait=False)

        epics.ca.poll()
        o_x = {}
        o_y = {}
        o = {}
        for c in self.ch_x:
            name = epics.ca.name(c).replace(":rdX","")
            x = epics.ca.get_complete(c)
            o_x[name] = x
        for c in self.ch_y:
            name = epics.ca.name(c).replace(":rdY","")
            y = epics.ca.get_complete(c)
            o_y[name] = y
        
        for c in o_x.keys():
            off = self.offsets[c]
            o[c] = (o_x[c] - off[0],o_y[c] - off[1])
            
        return o


#orb = OrbitData(['BPMZ3T3R','BPMZ7D1R'])
#o = orb.get()
#print(o)



class BESSYMachineInterface(MachineInterface):
    """
    Machine Interface for European XFEL
    """

    def __init__(self, args=None):
        super(BESSYMachineInterface, self).__init__(args=args)
        if 'epics' not in sys.modules:
            print('error importing EPICS library')
        self.logbook = "xfellog"
        self.allow_star_operation = True
        self.hide_section_selection = True
        self.hide_close_trajectory = True
        self.hide_xfel_specific = True
        self.hide_dispersion_tab = True
        self.twiss_periodic = True
        self.analyse_correction = False
        self.uncheck_upstream_bpms = False # uncheck bpms upstream the first corrector
        self.orm_method = RingRM
        self.drm_method = LinacDisperseSimRM
        self.orbit_data = OrbitData()
        self.corrector_data = CorrectorData()
        self.read_offset_orbit()
        self.conversion()
        self.lattice_manager = lattice_manager
        self.devices = devices

    def conversion(self):
        filename = "mint/conversion_factor_cor.csv"
        with open(filename, 'r') as f:
            lines = f.readlines()
        self.corr_conversion = {}
        for line in lines:
            ll = line.split()
            name = ll[0].replace("M", "P")
            self.corr_conversion[name] = [float(ll[1]), float(ll[2])]
        #print(cor)

    def read_offset_orbit(self):
        filename = "/opt/OPI/MapperApplications/conf/Orbit/SR/RefOrbit.Dat"
        #filename = "/opt/OPI/MapperApplications/conf/Orbit/SR/BBA-Reference-Data/BBA-11BPMOFF.SET"

        isfile = os.path.isfile(filename)
        a = {}
        if isfile:
            for l in open(filename).read().split('\n'):
                ll = l.split()
                if len(ll) <= 2: continue
                a[ll[0]] = [float(ll[1]), float(ll[2])]

        self.offset_orbit = a

    def get_value(self, channel):
        """
        Getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        logger.debug(" get_value: channel" + channel)
        val = epics.PV(channel).get()
        # print(channel, "   TIMESTAMP:",  val["timestamp"])
        #print(channel, " val = ", val)
        return val

    def set_value(self, channel, val):
        """
        Method to set value to a channel

        :param channel: (str) String of the devices name used in doocs
        :param val: value
        :return: None
        """
        # print("SETTING")
        epics.PV(channel).put(val)
        return

    def get_raw_value(self, channel):
        """
        Getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        logger.debug(" get_raw_value: channel" + channel)
        val = pydoocs.read(channel)
        return val

    def get_charge(self):
        return 1

    def send_to_logbook(self, *args, **kwargs):
        """
        Send information to the electronic logbook.

        :param args:
            Values sent to the method without keywork
        :param kwargs:
            Dictionary with key value pairs representing all the metadata
            that is available for the entry.
        :return: bool
            True when the entry was successfully generated, False otherwise.
        """
        pass


# test interface


class BESSYTestInterface(BESSYMachineInterface):
    """
    Machine interface for testing
    """

    def __init__(self, args=None):
        super(BESSYTestInterface, self).__init__(args=args)
        self.data = 1.

        self.allow_star_operation = False
        self.hide_section_selection = True
        self.hide_close_trajectory = True
        self.hide_xfel_specific = True
        self.hide_dispersion_tab = True
        self.twiss_periodic = True
        self.analyse_correction = False
        self.orm_method = RingRM
        self.drm_method = LinacDisperseSimRM
        self.orbit_data = OrbitData()
        self.corrector_data = CorrectorData()
        self.read_offset_orbit()
        self.conversion()

    def get_alarms(self):
        return np.random.rand(4)  # 0.0, 0.0, 0.0, 0.0]

    def get_value(self, device_name):
        """
        Testing getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        # if "QUAD" in device_name:
        #    return 0
        return np.random.rand(1)[0] - 0.5  # self.data

    def set_value(self, device_name, val):
        """
        Testing Method to set value to a channel

        :param channel: (str) String of the devices name used in doocs
        :param val: value
        :return: None
        """
        # print("set:", device_name,  "-->", val)
        self.data += np.sqrt(val ** 2)
        return 0.0

    def get_bpms_xy(self, bpms):
        """
        Testing method for getting bmps data

        :param bpms: list of string. BPMs names
        :return: X, Y - two arrays in [m]
        """
        X = np.zeros(len(bpms))
        Y = np.zeros(len(bpms))
        return X, Y

    def get_charge(self):
        return 0

    @staticmethod
    def send_to_logbook(*args, **kwargs):
        """
        Send information to the electronic logbook.

        :param args:
            Values sent to the method without keywork
        :param kwargs:
            Dictionary with key value pairs representing all the metadata
            that is available for the entry.
        :return: bool
            True when the entry was successfully generated, False otherwise.
        """
        author = kwargs.get('author', '')
        title = kwargs.get('title', '')
        severity = kwargs.get('severity', '')
        text = kwargs.get('text', '')
        elog = kwargs.get('elog', '')
        image = kwargs.get('image', None)

        # TODO: @sergey.tomin Figure out what to do for logbook at the TestMachineInterface
        print('Send to Logbook not implemented for TestMachineInterface.')
        return True
