'''
Created on Mar 13, 2014

@author: Onur
'''

import urllib2 
from time import sleep
from threading import Thread
from domain.CustomClient import CustomClient

class HTTPClient(CustomClient):
    '''
    classdocs
    '''
    
    CHECK_TIME = 10
    __address = None
    __id = None 
    __lastCmd = []
    __lastCmdId = 0
    __isNewCmd = False
        
    def __init__(self, ip, port):
        self.__address = (ip, port)

    def connect(self):
        response = urllib2.urlopen("http://{0}:{1}/com/getid".format(self.__address[0], self.__address[1]))
        self.__id = response.read()
        print self.__id
    
    def disconnect(self):
        pass
    
    def waitForCommand(self):
        """ Creates a thread to wait incoming commands.
            Returns the command as it arrives."""
        
        t = Thread(target = self.__fetchCommand)
        t.start()
        t.join()
        
        if self.__isNewCmd:
            self.__isNewCmd = False
            return self.__lastCmd.pop()
        else:
            self.connect()
            return self.waitForCommand()
    
    def __fetchCommand(self):        
        while True:
            response = urllib2.urlopen("http://{0}:{1}/com/{2}".format(self.__address[0], self.__address[1], self.__id))
            
            try:
                data = response.read()
                data = data.split('\n')

                if int(data[0]) > self.__lastCmdId:
                    self.__lastCmdId = self.__lastCmdId + 1
                      
                    if data[1] == "init":
                        print "init"
                    else:
                        self.__lastCmd.append(data[1])
                        self.__isNewCmd = True
                        return
            except URLError, e:
                return
            sleep(self.CHECK_TIME)
    
    def sendResponse(self, data):
        """ Sends the data to the server."""
        pass
        
