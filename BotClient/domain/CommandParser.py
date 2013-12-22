'''
Created on Dec 21, 2013

@author: Onur
'''

from base64 import b64decode

class CommandParser(object):
    """ Responsible for parsing incoming commands.
        
        The class is able to parse base64 encoded,
        comma separated commands and arguments."""


    def __init__(self):
        """ Default constructor"""
        pass
    
    @staticmethod
    def parseCommand(rawcmd):
        """ Base64 decodes and splits a command by comma.
            Returns the command code and arguments as a list."""        
        return b64decode(rawcmd).split(',')
                
        