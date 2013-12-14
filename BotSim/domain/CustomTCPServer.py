'''
Created on Dec 11, 2013

@author: Onur
'''

from socket import socket
from CustomTCPRequestHandler import CustomTCPRequestHandler
from threading import Thread

class CustomTCPServer(object):
    '''
    classdocs
    '''
    GET_BUFFER = 1204
    __address = None
    __clientPool = []
    __threadingServer = None 
    __serverSocket = None     
    __isRunning = True
    
    def __init__(self, address, port):
        '''
        Constructor
        '''        
        self.__address = (address, port)
        self.__serverSocket = socket()        
    
    def __run(self):
      
        self.__serverSocket.bind(self.__address)
        self.__serverSocket.listen(5)
        
        while self.__isRunning:            
            clientSocket, address = self.__serverSocket.accept()
            newClient = CustomTCPRequestHandler(clientSocket, address)            
            self.__clientPool.append(newClient)             
            newClient.start()                                                      
            
            
    def startServer(self):
        self.__isRunning = True
        self.__threadingServer = Thread(target=self.__run)
        self.__threadingServer.start()        
                
    def stopServer(self):            
        print self.__clientPool    
        for client in self.__clientPool:                       
            client.socket.close()
            client.stop()            
        
        self.__serverSocket.close()
        self.__isRunning = False
        self.__threadingServer.join()
        self.__clientPool = []        
    
    def restartServer(self):
        self.stopServer()
        self.startServer()
    
    def getClient(self, clientID):
        return self.__clientPool[clientID].socket
    
    def getClientCount(self):
        return len(self.__clientPool)
    
    def sendData(self, clientID, data):
        self.__clientPool[clientID].socket.send(data)
    
    def getData(self, clientID):
        return self.__clientPool[clientID].socket.recv(self.GET_BUFFER)
    
    def getAddress(self):
        return self.__address
            
        