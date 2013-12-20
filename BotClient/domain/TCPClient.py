'''
Created on Dec 20, 2013

@author: Onur
'''

import socket
from threading import Thread

class TCPClient(object):
    '''
    classdocs
    '''

    __serverName = None    
    __serverPort = None
    __csocket = None
    __serverResponse = []

    def __init__(self, serverName, serverPort):
        '''
        Constructor
        '''        
        self.__serverName = serverName
        self.__serverPort = serverPort
    
    def connect(self):
        self.__csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__csocket.connect((self.__serverName, self.__serverPort))
        self.__csocket.send("Hi server\n")
    
    def disconnect(self):
        self.__csocket.close()
        
    def waitForCommand(self):
        t = Thread(target = self.__run)
        t.start()
        t.join()
        return self.__serverResponse.pop()
    
    def __run(self):        
        self.__serverResponse.append(self.__csocket.recv(1024))
        
        
    def sendResponse(self, data):
        self.__csocket.send(data)
