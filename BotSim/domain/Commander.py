'''
Created on Dec 14, 2013

@author: Onur
'''

class Commander(object):
    '''
    classdocs
    '''
    
    __server = None

    def __init__(self, server):
        '''
        Constructor
        '''
        self.__server = server
    
    def listClients(self):
        for i in range(self.__server.getClientCount()):
            print self.__server.getClient(i).getsockname() 
    
    def sendCommand(self, interval, cmd):
        for i in range(interval[0], interval[1]+1):
            self.__server.sendData(i, cmd)
        
        return True
            