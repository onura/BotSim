'''
Created on Apr 24, 2014

@author: root
'''
import unittest
from domain.HashCrackUtils import HashCrackUtils 
from numpy.lib.tests.test_format import assert_equal


class Test(unittest.TestCase):


    def testSplit(self):
        inwl = "wlist.txt"
        client_count = 3
        hcutils = HashCrackUtils()
        splittedList = hcutils.splitFile(inwl, client_count)
        assert_equal(len(splittedList), client_count)
        print splittedList
                


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()