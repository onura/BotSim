'''
Created on Dec 20, 2013

@author: Onur
'''
import unittest
from domain.HTTPClient import HTTPClient
from domain.Bot import Bot


class Test(unittest.TestCase):


    def testHTTPConnection(self):
        bot = Bot(HTTPClient('127.0.0.1', 80))
        bot.activate()

    def CommandParser(self):
        bot = Bot(HTTPClient('127.0.0.1', 80))
        bot.activate()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()