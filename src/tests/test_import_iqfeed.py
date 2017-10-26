# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:19:10 2017

@author: pashute
"""
'''
  see youtube: python unitests https://www.youtube.com/watch?v=6tNS--WetLI
  testcase documentation: https://docs.python.org/2/library/unittest.html#unittest.TestCase
  python -m unittest test_...
'''
import unittest

class TestIqFeedImport(unittest.TestCase):
    def test_import_iqfeed(self):
        result = false  // failing by design
        assertTrue(result)
        
    def test_import_feeds(self):
        result = false // failing by design
        assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()