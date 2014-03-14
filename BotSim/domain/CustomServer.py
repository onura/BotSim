'''
Created on Mar 10, 2014

@author: Onur
'''

from abc import ABCMeta, abstractmethod


class CustomServer(object):
    '''
    classdocs
    '''
    
    __metaclass__ = ABCMeta 


    @abstractmethod   
    def startServer(self):
        """Starts the server."""
        pass
    
    @abstractmethod
    def stopServer(self):    
        """Stops the server and cleans the client pool"""
        pass        
    
    @abstractmethod
    def restartServer(self):
        """ Restarts to server."""
        pass
    
       
    @abstractmethod
    def getClientCount(self):
        """ Returns the total connected client count."""
        pass
    
    @abstractmethod
    def sendData(self, clientID, data):
        """ Sends data to the client with the right id."""
        pass
    
    @abstractmethod
    def getData(self, clientID):
        """ Gets data from the client with the right id. """
        pass
    
    @abstractmethod
    def getAddress(self):
        """ Returns the server's address port couple."""
        pass
    
    @abstractmethod        
    def getClientsList(self):
        """ Returns the IP addresses of clients'."""
        pass
    
    @abstractmethod 
    def getClientIds(self):
        pass