'''
Created on Dec 14, 2013

@author: Onur
'''
import unittest, time
from domain.CustomHTTPServer import CustomHTTPServer
from domain.Commander import Commander
from domain.Command import Command

class Test(unittest.TestCase):


    def ListClients(self):
        server = CustomHTTPServer('0.0.0.0', 80)
        server.startServer()
        commander = Commander(server)
        
        time.sleep(20)
        self.assertGreater(server.getClientCount(), 0, "no client")
        
        commander.listClients()
        server.stopServer()
    
    def testSendCommands(self):
        server = CustomHTTPServer('0.0.0.0', 80)
        server.startServer()
        commander = Commander(server)
        
        time.sleep(8)
        
        self.assertTrue(commander.sendCommand((10000,99999), Command("hi", "args")), "command sending problem")
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testListClients']
    unittest.main()