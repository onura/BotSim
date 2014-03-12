'''
Created on Dec 14, 2013

@author: Onur
'''
import unittest, time
from domain.CustomHTTPServer import CustomHTTPServer
from domain.Commander import Commander

class Test(unittest.TestCase):


    def testListClients(self):
        server = CustomHTTPServer('0.0.0.0', 80)
        server.startServer()
        commander = Commander(server)
        
        time.sleep(20)
        self.assertGreater(server.getClientCount(), 0, "no client")
        
        commander.listClients()
        server.stopServer()
    
    def SendCommands(self):
        server = CustomHTTPServer('0.0.0.0', 80)
        server.startServer()
        commander = Commander(server)
        
        time.sleep(8)
        
        self.assertTrue(commander.sendCommand((0,0), "cmd 1"), "command sending problem")
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testListClients']
    unittest.main()