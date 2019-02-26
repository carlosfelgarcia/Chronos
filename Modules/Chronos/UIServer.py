"""Server for multithreaded UI."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class UIServer(object):
    """Server that handles comunications to different UI clients."""

    def __init__(self, main, host='localHost', port=2243, bufferSize=1024, maxThreads=2):
        """Constuctor."""
        self.__main = main
        self.__bufferSize = bufferSize
        self.__serverSocket = socket(AF_INET, SOCK_STREAM)
        self.startServer(host, port, maxThreads)
        self.__serverSocket.close()

    def startServer(self, host, port, maxThreads):
        """Start the server and listen for new clients in the specified port.

        :param host: Host name of the server.
        :type host: str
        :param port: Port that connects the server.
        :type port: int
        :param maxThreads: Maximum number of clients.
        :type maxThreads: int
        """
        self.__serverSocket.bind((host, port))
        self.__serverSocket.listen(maxThreads)
        acceptConnections = Thread(target=self.getConnections)
        acceptConnections.start()
        acceptConnections.join()

    def getConnections(self):
        """Handle the connections of the clients."""
        while True:
            clientUI, clientUIAddress = self.__serverSocket.accept()
            print("{client} has connected.".format(client=clientUIAddress))
            Thread(target=self.clientConnection, args=(clientUI,)).start()

    def clientConnection(self, client):
        """Recived all the commands from the client."""
        while True:
            cmd = client.recv(self.__bufferSize).decode('UTF-8')
            if cmd == 'quit':
                client.close()
                break
            elif cmd == 'current':
                current = str(self.__main.getCurrentTimePerProcess())
                client.send(bytes(current, "utf8"))
            else:
                client.send(bytes("Command no implemented",  "utf8"))
