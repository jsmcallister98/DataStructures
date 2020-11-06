import unittest
from queue_array import *


class TestLab3(unittest.TestCase):
    def test_queue(self):
        """Trivial test to ensure method names and parameters are correct"""
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        q1 = Queue(5)
        self.assertEqual(q1.num_items, 0)
        self.assertEqual(q1.items, [None] * 5)
        self.assertEqual(q1.front, 0)
        self.assertEqual(q1.rear, 0)
        self.assertEqual(q1.__repr__(), "Queue(5, [])")
        q2 = Queue(5, [1, 2])
        self.assertEqual(q2.num_items, 2)
        self.assertEqual(q2.items, [1, 2, None, None, None])
        self.assertEqual(q2.front, 0)
        self.assertEqual(q2.rear, 2)

    def test_empty(self):
        # test empty queue
        q1 = Queue(5)
        self.assertTrue(q1.is_empty())
        # test non-empty queue
        q2 = Queue(5, [1])
        self.assertFalse(q2.is_empty())
        # test full queue
        q3 = Queue(3, [1, 2, 3])
        self.assertFalse(q3.is_empty())
        # test after dequeue last item
        q2.dequeue()
        self.assertTrue(q2.is_empty())
        # test after enqueue first item
        q1.enqueue(1)
        self.assertFalse(q1.is_empty())

    def test_full(self):
        # test empty queue
        q1 = Queue(5)
        self.assertFalse(q1.is_full())
        # test non-empty queue
        q2 = Queue(3, [1, 2])
        self.assertFalse(q2.is_full())
        # test full queue
        q3 = Queue(3, [1, 2, 3])
        self.assertTrue(q3.is_full())
        # test after dequeue last item
        q3.dequeue()
        self.assertFalse(q3.is_full())
        # test after enqueue last item
        q2.enqueue(3)
        self.assertTrue(q2.is_full())

    def test_enqueue(self):
        # test enqueue to empty queue
        q1 = Queue(3)
        q1.enqueue(1)
        self.assertEqual(q1.items, [1, None, None])
        # test enqueue in middle of queue
        q1.enqueue(2)
        self.assertEqual(q1.items, [1, 2, None])
        # test enqueue to fill queue
        q1.enqueue(3)
        self.assertEqual(q1.items, [1, 2, 3])
        # test enqueue to full queue
        with self.assertRaises(IndexError):
            q1.enqueue(4)
        # test wrap-around enqueue                 can you init [None, None, 3]?
        q2 = Queue(3, [1, 2, 3])
        q2.dequeue()
        q2.dequeue()
        q2.enqueue(1)
        self.assertEqual(q2.items, [1, None, 3])
        self.assertEqual(q2.get_items(), [3, 1])    # [3, 1] or [1, 3]?
        q2.enqueue(2)
        self.assertEqual(q2.items, [1, 2, 3])
        self.assertEqual(q2.get_items(), [3, 1, 2])

    def test_dequeue(self):
        # test empty queue
        q1 = Queue(3)
        with self.assertRaises(IndexError):
            q1.dequeue()
        # test queue with one item
        q2 = Queue(3, [1])
        self.assertEqual(q2.dequeue(), 1)
        self.assertEqual(q2.items, [None, None, None])
        self.assertEqual(q2.get_items(), [])
        # test full queue
        q3 = Queue(3, [1, 2, 3])
        self.assertEqual(q3.dequeue(), 1)
        self.assertEqual(q3.items, [None, 2, 3])
        self.assertEqual(q3.get_items(), [2, 3])
        # test wrap-around queue
        q4 = Queue(3, [1, 2, 3])
        q4.dequeue()
        q4.dequeue()
        self.assertEqual(q4.items, [None, None, 3])
        self.assertEqual(q4.get_items(), [3])
        q4.enqueue(1)
        q4.enqueue(2)
        q4.dequeue()
        self.assertEqual(q4.items, [1, 2, None])
        self.assertEqual(q4.get_items(), [1, 2])
        q4.dequeue()
        self.assertEqual(q4.items, [None, 2, None])
        self.assertEqual(q4.get_items(), [2])
        q4.enqueue(3)
        self.assertEqual(q3, q4)

    def test_size(self):
        # test empty queue
        q = Queue(3)
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
        q1 = Queue(5)
        self.assertTrue(q1.is_empty())
        self.assertFalse(q1.is_full())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        q2 = Queue(5, [1, 2])
        q2.enqueue(3)
        self.assertEqual(q1, q2)


if __name__ == '__main__':
    unittest.main()
