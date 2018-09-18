"""Interface for any OS module."""
from abc import ABCMeta, abstractmethod


class OSInterface(object):
    """
    Interface for any OS.

    Minimum functions required for any OS module (Windows, Lunix, Etc..).
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def getClosedProcesses(self):
        """Get the the processes that are closed.

        :return: A list of processes that no longer exist in the OS.
        :rtype: list
        """

    @abstractmethod
    def reloadProcess(self, osConfig):
        """Reload the processes running on the OS.

        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        """

    @abstractmethod
    def getProcessRunning(self):
        """
        Get all the process that are running in the system.

        It looks all the processes and base on a configuration file it filters
        the returning values.

        :returns: The process running on the system
        :rtype: list
        """
        pass

    @abstractmethod
    def getConfig(self):
        """Get the attributes that are set in the confugaration file.

        Atrributes that are coming from the user will averwritte any default value if matches the name.

        :return: The attributes that are set in the file
        :rtype: dict
        """
        pass

    @abstractmethod
    def setConfig(self, atrrs):
        """
        Set a configuration file to filter process and set other attributes.

        :param attrs: Attributes to set the dictionary.
        :type attrs: dict
        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass
