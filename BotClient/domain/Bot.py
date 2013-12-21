'''
Created on Dec 20, 2013

@author: Onur
'''

from CommandParser import CommandParser

class Bot(object):
    '''
    classdocs
    '''
    
    __client = None
    __modules = None

    def __init__(self, client):
        '''
        Constructor
        '''
        self.__client = client
        self.__modules = []
        
    def runCommand(self, cmd):
        print cmd
    
    def activate(self):
        self.__client.connect()
        while True:
            cmd = self.__client.waitForCommand()
            self.runCommand(CommandParser.parseCommand(cmd))
        