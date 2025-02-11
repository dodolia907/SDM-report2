#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_1 (self):
                self.assertEqual (1, calc(1,1))

        def test_2 (self):
                self.assertEqual (998001, calc(999,999))

        def test_3 (self):
                self.assertEqual (999, calc(999,1))
                self.assertEqual (999, calc(1,999))

        def test_4 (self):
                self.assertEqual (-1, calc(1000,1))
                self.assertEqual (-1, calc(1,1000))

        def test_5 (self):
                self.assertEqual (-1, calc(-1,150))
        
        def test_6 (self):
                self.assertEqual (-1, calc('hogehoge',150))
