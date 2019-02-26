"""Interface for any OS module."""
import abc


class OSInterface(abc.ABC):
    """
    Interface for any OS.

    Minimum functions required for any OS module (Windows, Lunix, Etc..).
    """

    @abc.abstractmethod
    def getClosedProcesses(self):
        """Get the the processes that are closed.

        :return: A list of processes that no longer exist in the OS.
        :rtype: list
        """
        pass

    @abc.abstractmethod
    def getActiveProcesses(self):
        """
        Get all the process that are running in the system.

        It looks all the processes and base on a configuration file it filters
        the returning values.

        :returns: The process running on the system
        :rtype: list
        """
        pass

    @abc.abstractmethod
    def getConfig(self):
        """Get the attributes that are set in the confugaration file.

        Atrributes that are coming from the user will averwritte any default value if matches the name.

        :return: The attributes that are set in the file
        :rtype: dict
        """
        pass

    @abc.abstractmethod
    def setConfig(self, atrrs):
        """
        Set a configuration file to filter process and set other attributes.

        :param attrs: Attributes to set the dictionary.
        :type attrs: dict
        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass
