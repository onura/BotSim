'''
Created on Mar 10, 2014

@author: root
'''
import unittest
from domain import CustomHTTPServer
import time

class Test(unittest.TestCase):


    def testHTTPServer(self):
        
        http = CustomHTTPServer.CustomHTTPServer("0.0.0.0", 80)
        http.startServer()
                
        time.sleep(10)
        
        
if __name__ == "__main__":
    unittest.main()