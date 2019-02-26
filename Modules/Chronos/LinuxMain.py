"""Main class to handle linux process."""
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
        self.__linuxConfig = LinuxConfig.LinuxConfig(self.__configFilePath)
        self.__linuxConfig.setDefaultAttrs()
        self.__linuxProcess = LinuxProcesses.LinuxProcesses(self.getConfig())

    def getClosedProcesses(self):
        """Get the the processes that are closed.

        :return: A list of processes that no longer exist in the OS.
        :rtype: list
        """
        return self.__linuxProcess.getClosedProcesses()

    def getActiveProcesses(self):
        """
        Get all the process that are running in the system.

        It looks all the processes and base on a configuration file it filters
        the returning values.

        :returns: The process running on the system
        :rtype: list
        """
        return self.__linuxProcess.getActiveProcesses()

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
