'''
Created on Dec 20, 2013

@author: Onur
'''
import unittest
from domain.TCPClient import TCPClient
from domain.Bot import Bot


class Test(unittest.TestCase):


    def testTCPConnection(self):
        bot = Bot(TCPClient('127.0.0.1', 555))
        bot.activate()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()