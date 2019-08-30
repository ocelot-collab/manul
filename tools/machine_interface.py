"""
S.Tomin, 2018, SPB lab
"""
try:
    import pydoocs
except:
    print("No pydoocs")
import numpy as np


class XFELMachineInterface():
    """
    Machine Interface for European XFEL
    """
    def __init__(self):
        pass

    def get_value(self, channel):
        """
        Getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        val = pydoocs.read(channel)
        return val["data"]

    def set_value(self, channel, val):
        """
        Method to set value to a channel

        :param channel: (str) String of the devices name used in doocs
        :param val: value
        :return: None
        """
        #print("SETTING")
        pydoocs.write(channel, val)
        return

class TestMachineInterface():
    """
    Machine interface for testing
    """
    def __init__(self):
        self.data = 1.
        pass

    def get_alarms(self):
        return np.random.rand(4)#0.0, 0.0, 0.0, 0.0]

    def get_value(self, device_name):
        """
        Testing getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        #if "QUAD" in device_name:
        #    return 0
        return np.random.rand(1)[0]-0.5 #self.data

    def set_value(self, device_name, val):
        """
        Testing Method to set value to a channel

        :param channel: (str) String of the devices name used in doocs
        :param val: value
        :return: None
        """
        #print("set:", device_name,  "-->", val)
        self.data += np.sqrt(val**2)
        return 0.0
