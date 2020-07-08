import unittest2

from calc import *

class Calc_Test(unittest2.TestCase):

    simple_calc = Calc()

    def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract(3, 1), 2)

    def test_multiplication(self):
        self.assertEqual(self.simple_calc.multiplication(2, 2), 4)

    def test_division(self):
        self.assertEqual(self.simple_calc.division(4, 4), 1)