import Win


class OSFactory(object):


    def __init__(self):
        self._osdict = {'win32': Win.Win}

    def getOS(self, osName):
        return self._osdict[osName]
