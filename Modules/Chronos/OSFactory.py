"""Factory of OS."""
import WinMain
import LinuxMain


class OSFactory(object):
    """Factory that returns the class requiered."""

    def __init__(self):
        """Constructor."""
        self._osdict = {'win32': WinMain.WinMain, 'linux': LinuxMain.LinuxMain}

    def getOS(self, osName):
        """Return the required instance of classes in the factory not yet initialize."""
        return self._osdict[osName]
