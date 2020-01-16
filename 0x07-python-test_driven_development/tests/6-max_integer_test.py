#!/usr/bin/python3
"""This is a unittest for the max_integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This is a test class of methods running individual unittests.
    """
    def test_postive(self):
        """Test if max_integer handles positive max.
        """
        _list = [-1, 0, 1, 2]
        self.assertEqual(max_integer(_list), 2)

    def test_negative(self):
        """Test if max_integer handles negative max.
        """
        _list = [-9, -18, -27, -36]
        self.assertEqual(max_integer(_list), -9)

    def test_empty(self):
        """Test if max_integer handles an empty list.
        """
        _list = []
        self.assertIsNone(max_integer(_list))

    def test_one_elem(self):
        """Test if max_integer handles one item list.
        """
        _list = [9]
        self.assertEqual(max_integer(_list), 9)

    def test_str(self):
        """Test if max_integer handles str comparison.
        """
        _list = ['Adam', 'Eve']
        self.assertEqual(max_integer(_list), 'Eve')

    def test_chr(self):
        """Test if max_integer handles chr comparison.
        """
        _list = ['a', 'b', 'c']
        self.assertEqual(max_integer(_list), 'c')

    def test_mid_val(self):
        """Test if max_integer handles middle val as max
        """
        _list = [0, 1, 4, 2, 3]
        self.assertEqual(max_integer(_list), 4)

if __name__ is '__main__':
    unittest.main()
