'''
Created on Aug 10, 2018

@author: User
'''
# System imports
import sys

# Local import
import OSFactory


class TimeManager(object):
    """Time manager main class."""

    def __init__(self):
        """Constructor."""
        self._osFactory = OSFactory.OSFactory()
        self._os = self._getOS()
        self.run()

    def run(self):
        """Run the main app and start recording the processes use."""
        osConfig = self._os.getConfig()
        while True:
            try:
                cpuPercent, processName = self._os.getProcessRunning(osConfig)
            except TypeError:
                continue
            # TODO Sep 9 -> File system to save the info per day
            # 1. Look for the last process and base on the config file it can assume it is working on it (e.g. Maya, word, etc..)
            # 2. Maybe 30secs to one minute or more with high activity in the CPU
            print('process name -> ', processName)
            print('CPU --> ', cpuPercent)


    def _getOS(self):
        osName = sys.platform
        return self._osFactory.getOS(osName)()


if __name__ == '__main__':
    tm = TimeManager()
