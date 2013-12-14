'''
Created on Dec 14, 2013

@author: Onur
'''

from domain.Command import Command

class Controller(object):
    '''
    classdocs
    '''

    commander = None

    def __init__(self, commander):
        '''
        Constructor
        '''        
        self.commander = commander
    
    
    def waitAction(self):        
        cline = raw_input("Enter a command with parameters: ")        
        cmd, interval = self.prepCommand(cline)
        
        if interval is None: 
            self.localCommand(cmd)
        else:
            self.commander.sendCommand(interval, cmd)
        
    
    def prepCommand(self, cline):
        cmdSplitted = cline.split(" ")
        if cmdSplitted[0] == "l":
                return cmdSplitted[1:], None
        elif cmdSplitted[0] == "r":
            cmd = Command(cmdSplitted[1], cmdSplitted[4:])        
            return cmd, (int(cmdSplitted[2]), int(cmdSplitted[3]))
    
    def localCommand(self, cmd):
        print cmd
        if cmd[0] == "list-clients":
            self.commander.listClients()
            