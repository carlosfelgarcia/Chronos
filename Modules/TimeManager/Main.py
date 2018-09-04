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
            print(self._os.getProcessRunning(osConfig))

    def _getOS(self):
        osName = sys.platform
        return self._osFactory.getOS(osName)()


if __name__ == '__main__':
    tm = TimeManager()
