'''
Created on Mar 13, 2014

@author: Onur
'''

from abc import ABCMeta, abstractmethod

class CustomClient(object):
    '''
    classdocs
    '''
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        """ Closes the server connection socket."""
        pass
    
    @abstractmethod
    def waitForCommand(self):
        """ Creates a thread to wait incoming commands.
            Returns the command as it arrives."""
        pass
    
    @abstractmethod
    def sendResponse(self, data):
        """ Sends the data to the server."""
        pass
        