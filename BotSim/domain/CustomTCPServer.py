'''
Created on Dec 11, 2013

@author: Onur
'''

from socket import socket
from CustomTCPRequestHandler import CustomTCPRequestHandler
from threading import Thread

class CustomTCPServer(object):
    """ A custom TCP server to handle TCP connections
        without closing the connection.
        
        CustomTCPServer is able to send and receive data to/from clients
        without closing the connections. So that, call to home functionality 
        of bots are preserved.
        
        Attributes:
            GET_BUFFER: The size of sockets' receive buffers.
            __addres: The servers IP,port couple
            __clientPool: Pool of open request handlers' references.
            __threadingServer: The TCP server's thread.
            __isRunning: Indicates the server's status. 
    """
    GET_BUFFER = 1204
    __address = None
    __clientPool = []
    __threadingServer = None 
    __serverSocket = None     
    __isRunning = True
    
    def __init__(self, address, port):
        """ Initializes an address couple from address and port.
            Then creates a server socket."""
             
        self.__address = (address, port)
        self.__serverSocket = socket()        
    
    def __run(self):
        """ Binds the socket to the server address 
            and starts waiting for incoming connections.
            Creates a CustomTCPRequestHandler per connection. """      
        self.__serverSocket.bind(self.__address)
        self.__serverSocket.listen(5)
        
        while self.__isRunning:            
            clientSocket, address = self.__serverSocket.accept()
            newClient = CustomTCPRequestHandler(clientSocket, address)            
            self.__clientPool.append(newClient)             
            newClient.start()                                                      
            
            
    def startServer(self):
        """Starts the server."""
        self.__isRunning = True
        self.__threadingServer = Thread(target=self.__run)
        self.__threadingServer.start()        
                
    def stopServer(self):    
        """Stops the server and cleans the client pool"""
                
        print self.__clientPool    
        for client in self.__clientPool:                       
            client.socket.close()
            client.stop()            
        
        self.__serverSocket.close()
        self.__isRunning = False
        self.__threadingServer.join()
        self.__clientPool = []        
    
    def restartServer(self):
        """ Restarts to server."""
        self.stopServer()
        self.startServer()
    
    def getClient(self, clientID):
        """Returns the client socket of given client id"""
        return self.__clientPool[clientID].socket
    
    def getClientCount(self):
        """ Returns the total connected client count."""
        return len(self.__clientPool)
    
    def sendData(self, clientID, data):
        """ Sends data to the client with the right id."""
        self.__clientPool[clientID].socket.send(data)
    
    def getData(self, clientID):
        """ Gets data from the client with the right id. """
        return self.__clientPool[clientID].socket.recv(self.GET_BUFFER)
    
    def getAddress(self):
        """ Returns the server's address port couple."""
        return self.__address
            
    def getClientsList(self):
        """ Returns the IP addresses of clients'."""
        cList = []
        for i in range(self.getClientCount()):
            cList.append(self.getClient(i).getsockname())
        
        return cList         