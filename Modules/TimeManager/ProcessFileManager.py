"""This class manage the file system of the processes."""

# Standard imports
import os
import time
# import json
from datetime import datetime


class ProcessFileManager(object):
    """Manage the file system for each process and it's information."""

    def __init__(self):
        """Constructor."""
        self.__processes = {}
        # TODO: Support for dropbox and/or aws
        self.__processFile = os.path.join(os.path.dirname(__file__), "processes.json")
        self.__todayDate = datetime.today().strftime('%Y-%m-%d')

    def getProcessFile(self):
        """Get the file that have all the information of the processes."""
        return self.__processFile

    def getProcessSession(self):
        """Get current session (in place for debuging, this will be the data that get save in the json file)."""
        return self.__processes

    def registerActiveProcess(self, processName, processId):
        """Register the active processes.

        It check if the process to be register exist, then it checks if the last session was closed.

        :param processName: The name of the process to be register.
        :type processName: str
        :param processId: The process id to get register.
        :type processId: int
        """
        startTime = time.time()
        if processId not in self.__processes:
            self.__processes[processId] = {
                self.__todayDate: [
                    {
                        'startTime': startTime,
                        'name': processName
                    }
                ]
            }
        else:
            currentProcess = self.__processes[processId][self.__todayDate]

            # Check if the last created has been closed
            if 'endTime' not in currentProcess[-1]:
                return

            currentProcess.append(
                {
                    'startTime': startTime,
                    'name': processName
                }
            )

    def stopProcesses(self, processIds):
        """Stop the process base on a specific id.

        Add the information of the end time for the last session of the specified process.

        :param processIds: A list of ids to be closed.
        :type processIds: list
        """
        endTime = time.time()
        # The current process is the latest that start
        for id in processIds:
            self.__processes[id][self.__todayDate][-1]['endTime'] = endTime
