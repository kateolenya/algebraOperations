#!/usr/bin/python3

import unittest
from algebra_operations import *

class TestAlgebraFucntions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_sub(self):
        self.assertEqual(sub(2, 3), 2 - 3)
        self.assertEqual(sub(2, -3), 2 - (-3))
        self.assertEqual(sub(-2, 3), -2 - 3)
        self.assertEqual(sub(-2, -3), -2 - (-3))
        self.assertEqual(sub(2, 0), 2 - 0)
        self.assertEqual(sub(0, 3), 0 - 3)

    def test_mult(self):
        self.assertEqual(mult(2, 3), 2 * 3)
        self.assertEqual(mult(2, -3), 2 * -3)
        self.assertEqual(mult(-2, 3), -2 * 3)
        self.assertEqual(mult(-2, -3), -2 * -3)
        self.assertEqual(mult(2, 0), 2 * 0)
        self.assertEqual(mult(0, 3), 0 * 3)

    def test_div(self):
        self.assertEqual(div(6, 3), 6 // 3)
        self.assertEqual(div(6, -3), 6 // -3)
        self.assertEqual(div(6, 0), None)
        self.assertEqual(div(-6, 3), -6 // 3)
        self.assertEqual(div(-6, -3), -6 // -3)
        self.assertEqual(div(6, 4), 6 // 4)

    def test_modulo(self):
        self.assertEqual(mod(6, 4), 6 % 4)
        self.assertEqual(mod(6, 0), None)
        self.assertEqual(mod(-6, 4), -6 % 4)
        self.assertEqual(mod(6, -4), 6 % -4)
        self.assertEqual(mod(-6, -4), -6 % -4)

if __name__ == '__main__':
    unittest.main()
