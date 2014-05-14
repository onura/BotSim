'''
Created on Apr 24, 2014

@author: root
'''

import os
from subprocess import call
from glob import glob

class HashCrackUtils(object):
    """ Utility class for hash crack attacks.
        
        Attributes:
            DATA_DIR: data path
            WL_PREFIX: wordlist prefix 
    """
    
    DATA_DIR = "data"
    WL_PREFIX = "wl_"
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def splitFile(self, wlist, clientCount):
        """ Splits given wlist into the given count
            without breaking words. """
            
        path = os.getcwd() 
        os.chdir(path + "/" + self.DATA_DIR)
        
        oldFiles = glob(self.WL_PREFIX + "*")
        for oldFile in oldFiles:
            os.remove(oldFile)
        
        call(["split", "-n", "l/" + str(clientCount), wlist, self.WL_PREFIX]) 
  
        splittedList = glob(self.WL_PREFIX + "*")
        os.chdir(path)
        
        return splittedList
        
        
        