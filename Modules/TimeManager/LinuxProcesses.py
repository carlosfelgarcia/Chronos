"""Module to handle all the linux processes."""
import psutil
import time


class LinuxProcesses(object):
    """Handle all the process for linux operate system."""

    def getAllProcesses(self, osConfig):
        """
        Get all the processes and filter some of them.

        Saved the process running to be faster and then it renew them every 30 seconds.
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
                # In linux the inteval gets multiply by the real use, so 1% = 10%
                cpuPercent = round(parent.cpu_percent(interval=0.1)/10, 2)
            except psutil.NoSuchProcess:
                parents.remove(parent)
                continue
            if cpuPercent > 2.0:
                return (cpuPercent, parent.name())
        endTime = time.time()
