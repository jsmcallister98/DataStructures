import unittest

from queue_nodelist import *


class TestLab1(unittest.TestCase):
    def test_queue(self):
        """Trivial test to ensure method names and parameters are correct"""
        q = Queue()
        q.is_empty()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        q1 = Queue()
        self.assertEqual(q1.num_items, 0)
        self.assertEqual(q1.front, None)
        self.assertEqual(q1.rear, None)
        self.assertEqual(q1.__repr__(), "Queue(None, None)")
        q2 = Queue()
        self.assertEqual(q1.__eq__(q2), True)

    def test_empty(self):
        # test empty queue
        q = Queue()
        self.assertTrue(q.is_empty())
        # test non-empty queue
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        # test after dequeue lst item
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_enqueue(self):
        # test enqueue to empty queue
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.get_items(), [1])
        # test non-empty queue
        q.enqueue(2)
        self.assertEqual(q.get_items(), [1, 2])
        q.enqueue(3)
        self.assertEqual(q.get_items(), [1, 2, 3])

    def test_dequeue(self):
        # test empty queue
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()
        # test queue with one item
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.get_items(), [])
        # general cases
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.get_items(), [2, 3])
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.get_items(), [3])

    def test_size(self):
        # test empty queue
        q = Queue()
        self.assertEqual(q.size(), 0)
        # test after enqueue
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        q.enqueue(3)
        self.assertEqual(q.size(), 3)
        # test after dequeue
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertEqual(q.size(), 0)

    def test_examples(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        self.assertFalse(q1.is_empty())
        self.assertEqual(q1.size(), 3)
        self.assertEqual(q1.dequeue(), 1)
        q2 = Queue()
        q2.enqueue(2)
        q2.enqueue(3)
        self.assertEqual(q1, q2)


if __name__ == '__main__':
    unittest.main()
