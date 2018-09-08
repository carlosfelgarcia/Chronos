"""Main class to handle windows process."""
# Standard imports
import os

# Local imports
import LinuxProcesses
import LinuxConfig
from OSInterface import OSInterface


class LinuxMain(OSInterface):
    """Linux class."""

    def __init__(self):
        """Constructor."""
        self.__configFilePath = os.path.join(os.path.dirname(__file__), "linuxConfig.json")
        # Initialize instances
        self.__linuxProcess = LinuxProcesses.LinuxProcesses()
        self.__linuxConfig = LinuxConfig.LinuxConfig(self.__configFilePath)

        # Call default methods
        self.__linuxConfig.setDefaultAttrs()

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
        return self.__linuxProcess.getAllProcesses(osConfig)

    def getConfig(self):
        """Get the attributes that are set in the confugaration file.

        Atrributes that are coming from the user will averwritte any default value if matches the name.

        :return: The attributes that are set in the file
        :rtype: dict
        """
        return self.__linuxConfig.getConfig()

    def setConfig(self, atrrs):
        """
        Set a configuration file to filter process and set other attributes.

        :param attrs: Attributes to set the dictionary.
        :type attrs: dict
        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass
