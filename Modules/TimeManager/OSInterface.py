from abc import ABCMeta, abstractmethod


class OSInterface(object):
    """
    Interface for any OS.

    Minimum functions required for any OS module (Windows, Lunix, Etc..).
    """
    __metaclass__ = ABCMeta

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

    def setConfig(self, configFile):
        """
        Set a configuration file to filter process and set other attributes.

        Args:
            configFile (str): The configuration file to be set.

        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass
