import unittest
from binary_search_tree import *


class TestLab4(unittest.TestCase):

    def test_isempty(self):
        # empty tree
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        # non empty tree
        bst.insert(10)
        self.assertFalse(bst.is_empty())

    def test_search(self):
        # empty tree
        bst = BinarySearchTree()
        self.assertFalse(bst.search(10))
        # item in tree
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        self.assertTrue(bst.search(15))
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(10))
        self.assertTrue(bst.search(20))
        # item not in tree
        self.assertFalse(bst.search(25))
        self.assertFalse(bst.search(3))
        self.assertFalse(bst.search(12))

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        self.assertEqual(bst.inorder_list(), [5, 10, 15, 20, 25])
        bst.insert(17)
        self.assertEqual(bst.inorder_list(), [5, 10, 15, 17, 20, 25])
        bst.insert(5, "replaced")
        self.assertEqual(bst.find_min(), (5, "replaced"))

    def test_min(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_min(), None)
        bst.insert(10)
        self.assertEqual(bst.find_min(), (10, None))
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        bst.insert(1, 'test')
        self.assertEqual(bst.find_min(), (1, 'test'))

    def test_max(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_max(), None)
        bst.insert(10)
        self.assertEqual(bst.find_max(), (10, None))
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25, 'test')
        bst.insert(1)
        self.assertEqual(bst.find_max(), (25, 'test'))

    def test_tree_height(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        bst.insert(10)
        self.assertEqual(bst.tree_height(), 0)
        bst.insert(20)
        bst.insert(5)
        self.assertEqual(bst.tree_height(), 1)
        bst.insert(15)
        bst.insert(25)
        self.assertEqual(bst.tree_height(), 2)
        bst.insert(30)
        self.assertEqual(bst.tree_height(), 3)

    def test_inorder(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        self.assertEqual(bst.inorder_list(), [5, 10, 15, 20, 25])
        bst.insert(17)
        self.assertEqual(bst.inorder_list(), [5, 10, 15, 17, 20, 25])
        bst.insert(2)
        bst.insert(7)
        self.assertEqual(bst.inorder_list(), [2, 5, 7, 10, 15, 17, 20, 25])

    def test_preorder(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        self.assertEqual(bst.preorder_list(), [10, 5, 20, 15, 25])
        bst.insert(17)
        self.assertEqual(bst.preorder_list(), [10, 5, 20, 15, 17, 25])
        bst.insert(2)
        bst.insert(7)
        self.assertEqual(bst.preorder_list(), [10, 5, 2, 7, 20, 15, 17, 25])

    def test_level_order(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.level_order_list(), [])
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        self.assertEqual(bst.level_order_list(), [10, 5, 20, 15, 25])
        bst.insert(17)
        self.assertEqual(bst.level_order_list(), [10, 5, 20, 15, 25, 17])
        bst.insert(2)
        bst.insert(7)
        self.assertEqual(bst.level_order_list(), [10, 5, 20, 2, 7, 15, 25, 17])

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])


if __name__ == '__main__':
    unittest.main()
