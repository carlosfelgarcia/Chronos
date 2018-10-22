"""Module to handle all the linux processes."""
import psutil
import copy


class LinuxProcesses(object):
    """Handle all the process for linux operate system."""

    def __init__(self, osConfig):
        """Constructor."""
        self.__activeProcesses = []
        self.__osConfig = osConfig

    def getClosedProcesses(self):
        """Get the closed processes base on the lookup time."""
        # We are going to reset the object to an empty list, so it needs to be copied.
        closeProcesses = []
        print("LEN --> ", len(self.__activeProcesses))
        for process in self.__activeProcesses:
            print("name --> ", process.info["name"])
            if not psutil.pid_exists(process.info['pid']):
                closeProcesses.append(process)

        # Clean active process:
        for process in closeProcesses:
            self.__activeProcesses.remove(process)

        return closeProcesses

    def getActiveProcesses(self, ):
        """Reload the processes running on the OS.

        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        """
        processes = []
        for proc in psutil.process_iter(attrs=['name', 'status', 'pid']):
            if proc.info['status'] == psutil.STATUS_RUNNING:
                if any([proc.info["name"].startswith(p) for p in self.__osConfig['skipProcess']]):
                    continue
                processes.append(proc)
                if proc not in self.__activeProcesses:
                    self.__activeProcesses.append(proc)

        return processes
