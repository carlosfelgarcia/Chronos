"""This class manage the file system of the processes."""

# Standard imports
import os
import time
import json
from datetime import datetime


class ProcessFileManager(object):
    """Manage the file system for each process and it's information."""

    def __init__(self):
        """Constructor."""
        self.__processes = {}
        # TODO: Support for dropbox and/or aws
        self.__sessionFile = os.path.join(os.path.dirname(__file__), "processes.json")
        self.__todayDate = datetime.today().strftime('%Y-%m-%d')

    def getSessionFile(self):
        """Get the file that have all the information of the processes."""
        return self.__sessionFile

    def getProcessSession(self):
        """Get current session (in place for debuging, this will be the data that get save in the json file)."""
        return self.__processes

    def getSavedSession(self):
        """Get the session saved.

        :return: The session saved as a dictionary or None
        """
        if not os.path.exists(self.__sessionFile):
            return

        with open(self.__sessionFile) as f:
            session = json.load(f)

        return session

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
            if id not in self.__processes:
                # Case when the system start at the same time the process was closing, so the process was not capture
                continue
            self.__processes[id][self.__todayDate][-1]['endTime'] = endTime

    def saveSession(self):
        """Save the current session in a JSON file."""
        currentSession = self.__cleanSession()
        finalSession = self.__joinSessions(currentSession)
        with open(self.__sessionFile, 'w') as outfile:
            json.dump(finalSession, outfile)

    def __joinSessions(self, currentSession):
        """Join the session values of the current and the saved session.

        :param currentSession: The current session.
        :type currentSession: dict
        :return: The join between the current and the saved session.
        :rtype: dict
        """
        savedSession = self.getSavedSession()
        print("SAVED ---> ", savedSession)
        for date, processDict in currentSession.items():
            if date in savedSession:
                for processName, totalTime in processDict.items():
                    if processName in savedSession[date]:
                        savedSession[date][processName] += totalTime
                    else:
                        savedSession[date][processName] = totalTime
            else:
                savedSession.update(currentSession)

        return savedSession

    def __cleanSession(self):
        """Clean the process that have not finished nor closed from the current session."""
        finalSession = {}
        for pid, processesDict in self.__processes.items():
            for procDate, processes in processesDict.items():
                for process in processes:
                    if 'endTime' not in process:
                        process['endTime'] = time.time()

                    totalTime = round(process['endTime'] - process['startTime'])

                    if procDate not in finalSession:
                        finalSession[procDate] = {}
                    if process['name'] not in finalSession[procDate]:
                        finalSession[procDate][process['name']] = totalTime
                    else:
                        finalSession[procDate][process['name']] += totalTime
        return finalSession
