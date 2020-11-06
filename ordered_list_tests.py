import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_isempty(self):
        # test empty list
        list0 = OrderedList()
        self.assertTrue(list0.is_empty())
        # test list with one item
        list0.add(1)
        self.assertFalse(list0.is_empty())
        # list with more than one item
        list0.add(2)
        list0.add(3)
        self.assertFalse(list0.is_empty())

    def test_add(self):
        # add to empty list
        list0 = OrderedList()
        list0.add(1)
        self.assertEqual(list0.python_list(), [1])
        # add to non-empty list
        list0.add(2)
        list0.add(5)
        self.assertEqual(list0.python_list(), [1, 2, 5])
        # add duplicate item
        list0.add(2)
        self.assertEqual(list0.python_list(), [1, 2, 5])
        # add "in-between" item
        list0.add(3)
        self.assertEqual(list0.python_list(), [1, 2, 3, 5])
        # add to front
        list0.add(0)
        self.assertEqual(list0.python_list(), [0, 1, 2, 3, 5])

    def test_remove(self):
        # empty list
        list0 = OrderedList()
        self.assertFalse(list0.remove(0))
        list0.add(0)
        # list with one item
        self.assertTrue(list0.remove(0))
        list0.add(0)
        self.assertFalse(list0.remove(1))
        list0.add(0)
        list0.add(1)
        list0.add(2)
        list0.add(3)
        # front of list
        self.assertTrue(list0.remove(0))
        self.assertEqual(list0.python_list(), [1, 2, 3])
        # rear of list
        self.assertTrue(list0.remove(3))
        self.assertEqual(list0.python_list(), [1, 2])
        list0.add(3)
        # middle of list
        self.assertTrue(list0.remove(2))
        self.assertEqual(list0.python_list(), [1, 3])
        list0.add(2)
        list0.add(4)
        list0.remove(3)
        # item greater than largest item in list
        self.assertFalse(list0.remove(5))
        # item less than smallest item in list
        self.assertFalse(list0.remove(0))
        # item in middle of list, but not present in list
        self.assertFalse(list0.remove(3))

    def test_index(self):
        list0 = OrderedList()
        # empty list
        self.assertEqual(list0.index(0), None)
        list0.add(0)
        # one item list
        self.assertEqual(list0.index(0), 0)
        list0.add(1)
        list0.add(2)
        list0.add(4)
        list0.add(3)
        # multiple item list
        self.assertEqual(list0.index(0), 0)
        self.assertEqual(list0.index(4), 4)
        self.assertEqual(list0.index(2), 2)

    def test_pop(self):
        list0 = OrderedList()
        # empty list
        with self.assertRaises(IndexError):
            list0.pop(0)
        list0.add(1)
        # index too large
        with self.assertRaises(IndexError):
            list0.pop(2)
        # negative index
        with self.assertRaises(IndexError):
            list0.pop(-1)
        # one item list
        self.assertEqual(list0.pop(0), 1)
        self.assertEqual(list0.python_list(), [])
        list0.add(0)
        list0.add(1)
        list0.add(2)
        list0.add(3)
        list0.add(4)
        # multi item list
        self.assertEqual(list0.pop(0), 0)
        self.assertEqual(list0.python_list(), [1, 2, 3, 4])
        self.assertEqual(list0.pop(3), 4)
        self.assertEqual(list0.python_list(), [1, 2, 3])
        self.assertEqual(list0.pop(1), 2)
        self.assertEqual(list0.python_list(), [1, 3])

    def test_search(self):
        # empty list
        list0 = OrderedList()
        self.assertFalse(list0.search(0))
        # one item list
        list0.add(0)
        self.assertTrue(list0.search(0))
        self.assertFalse(list0.search(1))
        # multi item list
        list0.remove(0)
        list0.add(1)
        list0.add(2)
        list0.add(4)
        list0.add(5)
        self.assertTrue(list0.search(1))
        self.assertTrue(list0.search(5))
        self.assertTrue(list0.search(2))
        # item below minimum item in list
        self.assertFalse(list0.search(0))
        # item in middle of list, not present in list
        self.assertFalse(list0.search(3))
        # item larger than largest list item
        self.assertFalse(list0.search(6))

    def test_python_list(self):
        # empty list
        list0 = OrderedList()
        self.assertEqual(list0.python_list(), [])
        # one item
        list0.add(0)
        self.assertEqual(list0.python_list(), [0])
        # multiple items
        list0.add(1)
        list0.add(2)
        list0.add(3)
        list0.add(4)
        self.assertEqual(list0.python_list(), [0, 1, 2, 3, 4])

    def test_reverse_plist(self):
        # empty list
        list0 = OrderedList()
        self.assertEqual(list0.python_list_reversed(), [])
        # one item
        list0.add(0)
        self.assertEqual(list0.python_list_reversed(), [0])
        # multi item
        list0.add(1)
        list0.add(2)
        list0.add(3)
        list0.add(4)
        self.assertEqual(list0.python_list_reversed(), [4, 3, 2, 1, 0])

    def test_size(self):
        # empty list
        list0 = OrderedList()
        self.assertEqual(list0.size(), 0)
        # one item
        list0.add(0)
        self.assertEqual(list0.size(), 1)
        # multi item
        list0.add(1)
        list0.add(2)
        list0.add(3)
        list0.add(4)
        self.assertEqual(list0.size(), 5)

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)


if __name__ == '__main__':
    unittest.main()
