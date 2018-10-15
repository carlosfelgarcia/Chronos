"""Module to handle all the linux processes."""
import psutil
import copy


class LinuxProcesses(object):
    """Handle all the process for linux operate system."""

    def __init__(self, osConfig):
        """Constructor."""
        self.__closedProcessIds = []
        self.__activeProcesses = []
        self.__osConfig = osConfig

    def getClosedProcesses(self):
        """Get the closed processes base on the lookup time."""
        # We are going to reset the object to an empty list, so it needs to be copied.
        processesIds = copy.copy(self.__closedProcessIds)
        self.__closedProcessIds = []
        return processesIds

    def loadProcess(self, ):
        """Reload the processes running on the OS.

        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        """
        cacheProcess = []
        for proc in psutil.process_iter():
            process = self.__loadProcess(proc, cacheProcess)
            if process and process not in self.__activeProcesses:
                self.__activeProcesses.append(process)

        print("__activeProcesses --> ", self.__activeProcesses)

    def __loadProcess(self, process, cacheProcess):
        """TODO."""
        if not process or process in cacheProcess:
            return

        cacheProcess.append(process)

        # In linux the inteval gets multiply by the real use, so 1% = 10%
        cpuPercent = round(process.cpu_percent(interval=0.1)/10, 2)
        if cpuPercent > 2.0 and process.name() not in self.__osConfig['skipProcess']:
            return process
        else:
            self.__loadProcess(process.parent(), cacheProcess)

    def getAllProcesses(self):
        """Get all the processes running in the OS."""
        return self.__activeProcesses
        # for parent in self.__activeProcesses:
        #
        #
        #         cpuPercent = process
        #         # print("NAME ---> ", parent.name())
        #         # print("CPU ---> ", cpuPercent)
        #     except psutil.NoSuchProcess:
        #         self.__activeProcesses.remove(parent)
        #         self.__closedProcessIds.append(parent.pid)
        #         continue
        #     if cpuPercent > 2.0:
                # return parent
