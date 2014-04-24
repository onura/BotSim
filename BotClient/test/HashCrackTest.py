'''
Created on Dec 21, 2013

@author: root
'''
import unittest
from domain.modules.HashCrackModule import HashCrackModule


class Test(unittest.TestCase):


    def testModule(self):
        args = "--format=md5 --wordlist=/root/workspace/BotSim_git/BotSim/test/words.txt /root/workspace/BotSim_git/BotSim/test/hashes.txt"
        hcrack = HashCrackModule()
        hcrack.start(args.split())
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()