'''
Created on Dec 14, 2013

@author: Onur
'''

from domain.Command import Command
from domain.BotCommand import BOT_COMMAND
from domain.HashCrackUtils import HashCrackUtils

class Controller(object):
    """ Responsible for command parsing, and distributing.
        
        Controller gets commands from the botmaster, parses them
        and invokes appropriate methods to run either a local command 
        or send a remote one.
        
        Attributes:
            commander: A Commander object
    """

    commander = None

    def __init__(self, commander):
        """ Initializes with a Commander object """
        self.commander = commander
    
    
    def waitAction(self):
        """ Waits the botmaster to input a command, decides whether
            it's a local or remote command and calls relevant methods.
        """        
        cline = raw_input("Enter a command with parameters: ")        
        cmd, interval = self.prepCommand(cline)
        
        if interval is None: 
            self.localCommand(cmd)
        else:
            if BOT_COMMAND[cmd.cmd] == BOT_COMMAND['hcrack_start']:
                clients = self.commander.getServer().getClientsList()
                hcutils = HashCrackUtils()
                splittedList = hcutils.splitFile(cmd.arguments[1], len(clients))
                for i in range(len(clients)):
                    cmd.arguments[1] = splittedList[i]                    
                    self.commander.sendSingleCommand(int(clients[i]), cmd)
                     
            else:    
                self.commander.sendCommand(interval, cmd)         
        
    
    def prepCommand(self, cline):
        """Prepares a command to be run or sent"""
        cmdSplitted = cline.split(" ")
        if cmdSplitted[0] == "l":
                return cmdSplitted[1:], None
        elif cmdSplitted[0] == "r":
            cmd = Command(cmdSplitted[1], cmdSplitted[4:])        
            return cmd, (int(cmdSplitted[2]), int(cmdSplitted[3]))
    
    def localCommand(self, cmd):
        """Runs a local command"""
        if cmd[0] == "list-clients":
            self.commander.listClients()
            