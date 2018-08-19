"""Main class to handle windows process."""
import psutil
import time


class Win(object):
    """Win class."""

    SKIP = ['System Idle Process', 'System']
    RENEWPROCTIME = 30

    def __init__(self):
        """Constructor."""
        pass

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
            if endTime - startTime > self.RENEWPROCTIME:
                startTime = time.time()
                reloadProcess = True
            if reloadProcess:
                for proc in psutil.process_iter():
                    procParent = proc.parent()
                    if procParent is not None and procParent not in parents and procParent.name() not in self.SKIP:
                        parents.append(proc.parent())
                reloadProcess = False

            for parent in parents:
                try:
                    cpuPercent = parent.cpu_percent(interval=0.1)
                except psutil.NoSuchProcess:
                    parents.remove(parent)
                    continue
                if cpuPercent > 1.0:
                    print(cpuPercent, parent.name())
            endTime = time.time()
