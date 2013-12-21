'''
Created on Dec 14, 2013

@author: Onur
'''

from BotCommand import BOT_COMMAND
from base64 import b64encode

class Command(object):
    '''
    classdocs
    '''

    cmd = None
    arguments = []

    def __init__(self, cmd, arguments):
        '''
        Constructor
        '''
        self.cmd = cmd
        self.arguments = list(arguments)
    
    def __str__(self):
        retStr = BOT_COMMAND[self.cmd]
        for arg in self.arguments:
            retStr = str(retStr) + "," + arg
        
        return retStr
    
    def getEncodedCommand(self):
        return b64encode(self.__str__())
    