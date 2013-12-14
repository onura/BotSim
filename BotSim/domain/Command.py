'''
Created on Dec 14, 2013

@author: Onur
'''

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
        retStr = self.cmd
        for arg in self.arguments:
            retStr = retStr + "," + arg
        
        return retStr