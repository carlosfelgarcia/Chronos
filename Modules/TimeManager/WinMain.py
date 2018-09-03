"""Main class to handle windows process."""
import WinProcesses
from OSInterface import OSInterface


class WinMain(OSInterface):
    """Win class."""

    SKIP = ['System Idle Process', 'System']
    RENEWPROCTIME = 30

    def __init__(self):
        """Constructor."""
        self.__winProcess = WinProcesses.WinProcesses()

    def getProcessRunning(self):
        """
        Get all the process that are running in the system.

        It looks all the processes and base on a configuration file it filters
        the returning values.

        :returns: The process running on the system
        :rtype: list
        """
        # TODO: Get the configuration file
        return self.__winProcess.getAllProcesses()

    def setConfig(self, configFile):
        """
        Set a configuration file to filter process and set other attributes.

        Args:
            configFile (str): The configuration file to be set.

        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass
