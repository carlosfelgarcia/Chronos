#!/usr/bin/env python3.6
"""Main class of the Time Manager."""
# System imports
import sys
import time
import os
from threading import Thread

# Local import
import OSFactory
import ProcessFileManager
import TimeActivity
import UIServer


class TimeManager(object):
    """Time manager main class."""

    def __init__(self):
        """Constructor."""
        self.__osFactory = OSFactory.OSFactory()
        self.__processeFileManager = ProcessFileManager.ProcessFileManager()
        self.__timeActivity = TimeActivity.TimeActivity()
        self.__os = self.__getOS()
        self.__processCounter = {}

    def run(self):
        """Run the main app and start recording the processes use."""
        osConfig = self.__os.getConfig()
        while True:
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

            # Stop the process that are idle
            self.__processeFileManager.stopProcesses(processToClose)

            # Get active processes and register them
            processes = self.__os.getActiveProcesses()
            for process in processes:
                # Clean the name for windows processes
                procName = process.info['name'].lower().replace('.exe', '')
                self.__processeFileManager.registerActiveProcess(procName, process.info['pid'])
                self.__processCounter[process.pid] = 0

            # Save session
            self.saveSession()
            # Wait for lookup seconds to look for more processes
            time.sleep(osConfig['lookupTime'])

    def getCurrentTimePerProcess(self):
        """Calculate the time per process base on the current session."""
        return self.__timeActivity.getCurrentTimePerProcess(self.__processeFileManager.getProcessSession())

    def getWeeklyTime(self):
        """Calculate the time per process base on the current session."""
        savedSession = self.__processeFileManager.getSavedSession()
        return self.__timeActivity.getProcessesByTime(savedSession, days=7)

    def saveSession(self):
        """Save the current session in a JSON file."""
        self.__processeFileManager.saveSession()

    def __getOS(self):
        """Get the main OS module."""
        osName = sys.platform
        return self.__osFactory.getOS(osName)()


if __name__ == '__main__':
    # Set threads to each process so it will be faster and can handle infinte cycles on each thread
    tm = TimeManager()
    threadRun = Thread(target=tm.run)
    threadRun.start()
    threadServer = Thread(target=UIServer.UIServer, args=(tm,))
    threadServer.start()
