'''
Created on Mar 13, 2014

@author: Onur
'''

import httplib
from domain.CustomClient import CustomClient

class HTTPClient(CustomClient):
    '''
    classdocs
    '''
    
    __address = None
    __id = None 
        
    def __init__(self, ip, port):
        self.__address = (ip, port)

    def connect(self):
        conn = httplib.HTTPConnection(self.__address[0], self.__address[1])
        conn.request("GET", "/getid")
        response = conn.getresponse()
        self.__id = response.read()
    
    def disconnect(self):
        pass
    
    def waitForCommand(self):
        """ Creates a thread to wait incoming commands.
            Returns the command as it arrives."""
        pass
    
    def sendResponse(self, data):
        """ Sends the data to the server."""
        pass
        