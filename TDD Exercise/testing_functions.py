import unittest

from pytest import *

class testing(unittest.TestCase):

    calculating = math_functions()

    def test_sqrt(self):
        self.assertEqual(self.calculating.find_sqrt(16), 4)

    def test_ceil(self):
        self.assertEqual(self.calculating.find_ceil(3.44445), 3)


