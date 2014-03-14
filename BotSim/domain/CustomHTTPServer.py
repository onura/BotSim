'''
Created on Mar 10, 2014

@author: Onur
'''

import SocketServer
import os
from time import time, sleep
from threading import Thread
from domain.CustomServer import CustomServer
from domain.CustomHTTPRequestHandler import CustomHTTPRequestHandler

class CustomHTTPServer(CustomServer):
    '''
    classdocs
    '''

    __httpd = None
    __address = None
    __threadingServer = None
    __clientPool = None
    __accessChecker = None
    CLIENT_TIMEOUT = 120
    
    def __init__(self, ip, port):
        self.__address = (ip, port)
    
    def startServer(self):
        """Starts the server."""
        self.__httpd = SocketServer.TCPServer(self.__address, CustomHTTPRequestHandler)
        self.__threadingServer = Thread(target = self.__httpd.serve_forever)
        self.__threadingServer.start()
        
        if self.__accessChecker is None:
            self.__accessChecker = Thread(target = self.__checkLastAccess)
            self.__accessChecker.start()
        
    def stopServer(self):    
        self.__httpd.shutdown()
    
    def restartServer(self):
        """ Restarts to server."""
        self.stopServer()
        self.startServer()
    
    def getClientCount(self):
        """ Returns the total connected client count."""        
        return len(self.__clientPool)
    
    def sendData(self, clientID, data):
        """ Sends data to the client with the right id."""
        
        try:
            path = os.getcwd() + "/com/" + str(clientID)
            f = open(path, "r")
            lastCmd = int(f.readline()) + 1            
            f.close()
            f = open(path, "w")
            f.write('{}'.format(lastCmd))
            f.write("\n" + data)
            f.close()
            return True
        except:
            print 
            print "sendData exception"
            return False
    
    def getData(self, clientID):
        """ Gets data from the client with the right id. """
        pass
    
    def getAddress(self):
        """ Returns the server's address port couple."""
        return self.__address
    
    def getClientsList(self):
        """ Returns the IP addresses of clients'."""
        return self.__clientPool 
        
    
    def __checkLastAccess(self):
        path = os.getcwd() + "/com/"
        
        while True:
            fileList = os.listdir(path)
            t = time()
            
            newList = []
            for f in fileList:
                if f == "getid":
                    continue
                
                if t - os.stat(path + f).st_atime < self.CLIENT_TIMEOUT:
                    newList.append(f)
                else:
                    os.remove(path + f)
            
            self.__clientPool = newList 
            sleep(2)
            
    def getClientIds(self):
        self.__clientPool.sort()
        return self.__clientPool