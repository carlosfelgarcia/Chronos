"""Module to handle all the windows processes."""
import psutil
import time


class LinuxProcesses(object):
    """Handle all the process for windows operate system."""

    __SKIP = ['System Idle Process', 'System']
    __RENEWPROCTIME = 30

    def getAllProcesses(self):
        """
        Get all the processes and filter some of them.

        Saved the process running to be faster and then it renew them every 30 seconds.
        """
        parents = []
        startTime = time.time()
        endTime = 0
        reloadProcess = True
        while True:
            if endTime - startTime > self.__RENEWPROCTIME:
                startTime = time.time()
                reloadProcess = True
            if reloadProcess:
                for proc in psutil.process_iter():
                    procParent = proc.parent()
                    if procParent is not None and procParent not in parents and procParent.name() not in self.__SKIP:
                        parents.append(proc.parent())
                reloadProcess = False

            for parent in parents:
                try:
                    # In linux the inteval gets multiply so 1% = 10%
                    cpuPercent = round(parent.cpu_percent(interval=0.1)/10, 2)
                except psutil.NoSuchProcess:
                    parents.remove(parent)
                    continue
                if cpuPercent > 2.0:
                    print(cpuPercent, parent.name())
            endTime = time.time()
