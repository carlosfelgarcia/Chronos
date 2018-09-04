"""Main class to handle windows process."""
# Local imports
import WinProcesses
import WinConfig
from OSInterface import OSInterface

# Standard imports
import os


class WinMain(OSInterface):
    """Win class."""

    def __init__(self):
        """Constructor."""
        self.__configFilePath = os.path.join(os.path.dirname(__file__), "winConfig.json")
        # Initialize instances
        self.__winProcess = WinProcesses.WinProcesses()
        self.__winConfig = WinConfig.WinConfig(self.__configFilePath)

        # Call default methods
        self.__winConfig.setDefaultAttrs()

    def getProcessRunning(self, osConfig):
        """
        Get all the process that are running in the system.

        It looks all the processes and base on a configuration file it filters
        the returning values.

        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        :returns: The process running on the system
        :rtype: list
        """
        return self.__winProcess.getAllProcesses(osConfig)

    def getConfig(self):
        """Get the attributes that are set in the confugaration file.

        Atrributes that are coming from the user will averwritte any default value if matches the name.

        :return: The attributes that are set in the file
        :rtype: dict
        """
        return self.__winConfig.getConfig()

    def setConfig(self, atrrs):
        """
        Set a configuration file to filter process and set other attributes.

        Args:
            attrs (dict): Attributes to set the dictionary.

        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass
