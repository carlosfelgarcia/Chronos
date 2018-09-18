"""Module to handle all the linux processes."""
import psutil
import copy


class LinuxProcesses(object):
    """Handle all the process for linux operate system."""

    def __init__(self):
        """Constructor."""
        self.__closedProcessIds = []
        self.__parents = []

    def getClosedProcesses(self):
        """Get the closed processes base on the lookup time."""
        # We are going to reset the object to an empty list, so it needs to be copied.
        processesIds = copy.copy(self.__closedProcessIds)
        self.__closedProcessIds = []
        return processesIds

    def reloadProcess(self, osConfig):
        """Reload the processes running on the OS.

        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        """
        for proc in psutil.process_iter():
            procParent = proc.parent()
            if procParent and procParent not in self.__parents and procParent.name() not in osConfig['skipProcess']:
                self.__parents.append(procParent)

    def getAllProcesses(self):
        """Get all the processes running in the OS."""
        if not self.__parents:
            print("No parents found :(")
            return
        for parent in self.__parents:
            try:
                # In linux the inteval gets multiply by the real use, so 1% = 10%
                cpuPercent = round(parent.cpu_percent(interval=0.1)/10, 2)
            except psutil.NoSuchProcess:
                self.__parents.remove(parent)
                self.__closedProcessIds.append(parent.pid)
                continue
            if cpuPercent > 2.0:
                return parent
