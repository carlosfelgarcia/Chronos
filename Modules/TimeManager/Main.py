'''
Created on Aug 10, 2018

@author: User
'''
# System imports
import sys

# Local import
import OSFactory


class TimeManager(object):
    """
    Time manager main class
    """

    def __init__(self):
        """
        Constructor
        """
        self._osFactory = OSFactory.OSFactory()
        self._os = self._getOS()
        self._os.getProcessRunning()
        # self._os.test()

    def _getOS(self):
        osName = sys.platform
        return self._osFactory.getOS(osName)()


if __name__ == '__main__':
    tm = TimeManager()
