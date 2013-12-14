'''
Created on Dec 11, 2013

@author: Onur
'''

import unittest, time
from domain import CustomTCPServer

class Test(unittest.TestCase): 
    
    def testTCPServerIP(self):
        server = CustomTCPServer.CustomTCPServer('localhost', 555)
        server.startServer()
                        
        print server.getAddress()
        self.assertEqual(server.getAddress()[0], "localhost", "unexpected ip")
                
        time.sleep(5)
        #server.stopServer()
    
    def TCPClientIP(self):                
                        
        server = CustomTCPServer.CustomTCPServer('localhost', 555)
        server.startServer()
       
        time.sleep(5) 
        print server.getClient(0).getsockname()
        self.assertEqual(server.getClient(0).getsockname()[0], "127.0.0.1", "unexpected ip")                
       
        #self.server.stopServer()


if __name__ == "__main__":
    
    unittest.main()