#!/usr/bin/python3
"""Interactive tests
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class InteractiveTestsMaxInteger(unittest.TestCase):
    """
    This class is a interactive test for the function
    max_integer(list=[])
    """
    def text_good_results(self):
        """
        Test for compare results
        """
        self.assertAlmostEquals(max_integer([10, 20, 30, 50]), 50)
        self.assertAlmostEquals(max_integer([50, 30, 10, 20]), 50)
        self.assertAlmostEquals(max_integer([30, 2, 34, 5]), 34)
        self.assertAlmostEquals(max_integer([-1, -2, -3, -5]), -1)
        self.assertAlmostEquals(max_integer([1.2, 2.2, 3.3, 5.5]), 5.5)
        self.assertAlmostEquals(max_integer([50]), 50)

    def text_empty(self):
        """
        Test for compares result when the list is empty
        """
        self.assertAlmostEquals(max_integer([]), None)

    def test_errors(self):
        """
        Test for
        """
        lista = [4, 4.5, "Hello", 10]
        with self.assertRaises(TypeError):
            max_integer(lista)

    def test_None(self):
        """
        Test for compare result with None like argument
        """
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
