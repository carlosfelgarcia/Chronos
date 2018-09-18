"""Main class of the Time Manager."""
# System imports
import sys
import time

# Local import
import OSFactory
import ProcessFileManager


class TimeManager(object):
    """Time manager main class."""

    def __init__(self):
        """Constructor."""
        self.__osFactory = OSFactory.OSFactory()
        self.__processeFileManager = ProcessFileManager.ProcessFileManager()
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
                print("COUNTER --> ", self.__processCounter)
                closedTimerStart = time.time()
                self.__os.reloadProcess(osConfig)
                processToClose = self.__os.getClosedProcesses()

                # Iterate over active processes and wait until 1 minute and half to declare it idle.
                for processId, counter in self.__processCounter.items():
                    if counter == 2:
                        processToClose.append(processId)
                        continue
                    self.__processCounter[processId] += 1

                # Clean the counter
                for id in processToClose:
                    if id in self.__processCounter:
                        del self.__processCounter[id]

                print("process to close --> ", processToClose)
                self.__processeFileManager.stopProcesses(processToClose)

            process = self.__os.getProcessRunning()
            if not process:
                closedTimerEnd = time.time()
                continue

            print("process ---> ", process)
            self.__processeFileManager.registerActiveProcess(process.name(), process.pid)
            self.__processCounter[process.pid] = 0
            print("Session ---> ", self.__processeFileManager.getProcessSession())
            closedTimerEnd = time.time()

    def __getOS(self):
        """Get the main OS module."""
        osName = sys.platform
        return self.__osFactory.getOS(osName)()


if __name__ == '__main__':
    tm = TimeManager()
