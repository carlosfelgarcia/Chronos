"""It handles all the logic to calculate the time spending on the process."""
# Standard imports
from datetime import datetime


class TimeActivity(object):
    """Class that will handle the logic of the processes."""

    def __init__(self):
        """Constructor. (place holder for now)."""
        self.__todayDate = datetime.today().strftime('%Y-%m-%d')

    def getCurrentTimePerProcess(self, session):
        """Calculate the time per process base on the current session.

        A session look like:
        {
        Pid:
            {
            <str date>:
                [
                    {
                        'startTime': 1538355688.982312,
                        'name': 'chrome'
                    }
                ]
            }

        :param session: The session of the current processes.
        :type session: dict
        :return timePerProcess: A dictionary with the name of the process and the total time in seconds.
        :rtype timePerProcess: dict
        """
        timePerProcess = {}

        for pid, processes in session.items():
            for procDate, processesData in processes.items():
                for processData in processesData:
                    if 'endTime' not in processData:
                        continue
                    processName = processData['name']
                    startTime = processData['startTime']
                    endTime = processData['endTime']
                    if processName not in timePerProcess:
                        timePerProcess[processName] = (endTime - startTime)
                    else:
                        timePerProcess[processName] += (endTime - startTime)

        return timePerProcess

    def getTimePerProcessWeek(self, session):
        """TODO."""
        # TODO
        pass
