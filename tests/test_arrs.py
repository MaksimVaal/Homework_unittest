import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        test_list = [1, 2, 3]
        self.assertEqual(arrs.get(test_list, 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get(test_list, -2), None)
        self.assertEqual(arrs.get(test_list, len(test_list), "test"), "test")

    def test_slice(self):
        test_list = [1, 2, 3]
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice(test_list, 1), [2, 3])
        self.assertEqual(arrs.my_slice(test_list), test_list)
        self.assertEqual(arrs.my_slice(test_list, 0, 0), [])
        self.assertEqual(arrs.my_slice(test_list, 1, len(test_list) + 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1, len(test_list) + 1), [])

