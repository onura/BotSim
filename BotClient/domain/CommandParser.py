'''
Created on Dec 21, 2013

@author: Onur
'''

from base64 import b64decode

class CommandParser(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def parseCommand(rawcmd):        
        return b64decode(rawcmd).split(',')
                
        