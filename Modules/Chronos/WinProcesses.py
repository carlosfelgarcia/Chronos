"""Module to handle all the windows processes."""
import psutil


class WinProcesses(object):
    """Handle all the process for windows operate system."""

    def __init__(self, osConfig):
        """Constructor."""
        self.__activeProcesses = []
        self.__osConfig = osConfig
        self.__totalCpus = psutil.cpu_count()

    def getClosedProcesses(self):
        """Get the closed processes base on the lookup time."""
        closeProcesses = []
        for process in self.__activeProcesses:
            if not psutil.pid_exists(process.info['pid']):
                closeProcesses.append(process)

        for process in closeProcesses:
            self.__activeProcesses.remove(process)

        return closeProcesses

    def getActiveProcesses(self, ):
        """Reload the processes running on the OS.

        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        """
        processes = []
        for proc in psutil.process_iter(attrs=['name', 'pid', 'username']):
            if not proc.info['username']:
                continue
            # Windows have give you the total on all threads.
            cpuPercent = proc.cpu_percent() / self.__totalCpus
            if cpuPercent > 2.0:
                if any([proc.info["name"].startswith(p) for p in self.__osConfig['skipProcess']]):
                    continue
                processes.append(proc)
                if proc not in self.__activeProcesses:
                    self.__activeProcesses.append(proc)

        return processes
