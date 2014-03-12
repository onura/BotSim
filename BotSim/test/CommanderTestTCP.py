'''
Created on Dec 14, 2013

@author: Onur
'''
import unittest, time
from domain.CustomTCPServer import CustomTCPServer
from domain.Commander import Commander

class Test(unittest.TestCase):


    def testListClients(self):
        server = CustomTCPServer('localhost', 555)
        server.startServer()
        commander = Commander(server)
        
        time.sleep(5)
        self.assertGreater(server.getClientCount(), 0, "no client")
        
        commander.listClients()
    
    def SendCommands(self):
        server = CustomTCPServer('localhost', 555)
        server.startServer()
        commander = Commander(server)
        
        time.sleep(8)
        
        self.assertTrue(commander.sendCommand((0,0), "cmd 1"), "command sending problem")
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testListClients']
    unittest.main()