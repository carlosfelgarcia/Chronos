"""Main class of the Time Manager."""
# System imports
import sys
import time

# Local import
import OSFactory
import ProcessFileManager
import TimeActivity

class TimeManager(object):
    """Time manager main class."""

    def __init__(self):
        """Constructor."""
        self.__osFactory = OSFactory.OSFactory()
        self.__processeFileManager = ProcessFileManager.ProcessFileManager()
        self.__timeActivity = TimeActivity.TimeActivity()
        self.__os = self.__getOS()
        self.__processCounter = {}
        self.run()

    def run(self):
        """Run the main app and start recording the processes use."""
        osConfig = self.__os.getConfig()
        closedTimerStart = time.time()
        # Initialize this variable with more value so it enter the first time
        closedTimerEnd = closedTimerStart + osConfig['lookupTime'] + 2
        while True:
            if closedTimerEnd - closedTimerStart > osConfig['lookupTime']:
                closedTimerStart = time.time()
                self.__os.reloadProcess(osConfig)
                processToClose = self.__os.getClosedProcesses()

                # Iterate over active processes and wait for the cycles setted to declare it idle.
                for processId, counter in self.__processCounter.items():
                    if counter == osConfig['idleCycles']:
                        processToClose.append(processId)
                        continue
                    self.__processCounter[processId] += 1

                # Clean the counter
                for id in processToClose:
                    if id in self.__processCounter:
                        del self.__processCounter[id]

                self.__processeFileManager.stopProcesses(processToClose)

            process = self.__os.getProcessRunning()
            if not process:
                closedTimerEnd = time.time()
                continue

            self.__processeFileManager.registerActiveProcess(process.name(), process.pid)
            self.__processCounter[process.pid] = 0
            self.getTimePerProcess()
            closedTimerEnd = time.time()

    def getTimePerProcess(self):
        """Calculate the time per process base on the session."""
        self.__timeActivity.getTimePerProcess(self.__processeFileManager.getProcessSession())

    def __getOS(self):
        """Get the main OS module."""
        osName = sys.platform
        return self.__osFactory.getOS(osName)()


if __name__ == '__main__':
    tm = TimeManager()
