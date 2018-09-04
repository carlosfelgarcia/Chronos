"""Module to handle all the windows processes."""
import psutil
import time


class WinProcesses(object):
    """Handle all the process for windows operate system."""

    def getAllProcesses(self, osConfig):
        """
        Get all the processes and filter some of them.

        Saved the process running to be faster and then it renew them every 30 seconds base on the attribute set.
        :param osConfig: The configuration load for the OS
        :type osConfig: dict
        """
        parents = []
        startTime = time.time()
        endTime = 0
        reloadProcess = True
        if endTime - startTime > osConfig['lookupTime']:
            startTime = time.time()
            reloadProcess = True
        if reloadProcess:
            for proc in psutil.process_iter():
                procParent = proc.parent()
                if procParent and procParent not in parents and procParent.name() not in osConfig['skipProcess']:
                    parents.append(proc.parent())
            reloadProcess = False

        for parent in parents:
            try:
                cpuPercent = parent.cpu_percent(interval=0.1)
            except psutil.NoSuchProcess:
                parents.remove(parent)
                continue
            if cpuPercent > 2.0:
                return (cpuPercent, parent.name())
            endTime = time.time()
