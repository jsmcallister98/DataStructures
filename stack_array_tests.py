import unittest
from stack_array import Stack


class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None] * 5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_is_empty(self):
        # test an empty stack
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        # test non-empty stack
        stack1 = Stack(5, [1, 2])
        self.assertFalse(stack1.is_empty())
        # test full stack
        full_stack = Stack(3, [1, 2, 3])
        self.assertFalse(full_stack.is_empty())

    def test_is_full(self):
        # test an empty stack
        stack = Stack(5)
        self.assertFalse(stack.is_full())
        # test non-empty stack
        stack1 = Stack(5, [1, 2])
        self.assertFalse(stack1.is_full())
        # test full stack
        full_stack = Stack(3, [1, 2, 3])
        self.assertTrue(full_stack.is_full())

    def test_push(self):
        # test first push
        stack = Stack(3)
        stack.push("item")
        self.assertEqual(stack.items, ["item", None, None])
        self.assertEqual(stack.num_items, 1)
        # test second push
        stack.push(2)
        self.assertEqual(stack.items, ["item", 2, None])
        self.assertEqual(stack.num_items, 2)
        # test push that reaches stack capacity
        stack.push(True)
        self.assertEqual(stack.items, ["item", 2, True])
        self.assertEqual(stack.num_items, 3)
        # test push when stack is full
        with self.assertRaises(IndexError):
            stack.push("too much!")

    def test_pop(self):
        # test empty stack
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.pop()
        # test stack with one item
        stack1 = Stack(3, [1])
        self.assertEqual(stack1.pop(), 1)
        self.assertEqual(stack1.items, [None, None, None])
        self.assertEqual(stack1.num_items, 0)
        # test a full stack
        full_stack = Stack(3, [1, 2, 3])
        self.assertEqual(full_stack.pop(), 3)
        self.assertEqual(full_stack.items, [1, 2, None])
        self.assertEqual(full_stack.num_items, 2)

    def test_peek(self):
        # test empty stack
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.peek()
        # test stack with one item
        stack1 = Stack(3, [1])
        self.assertEqual(stack1.peek(), 1)
        self.assertEqual(stack1.items, [1, None, None])
        # test full stack
        full_stack = Stack(3, [1, 2, 3])
        self.assertEqual(full_stack.peek(), 3)
        self.assertEqual(full_stack.items, [1, 2, 3])

    def test_size(self):
        # test empty stack
        stack = Stack(3)
        self.assertEqual(stack.size(), 0)
        # test stack with one item
        stack1 = Stack(3, [1])
        self.assertEqual(stack1.size(), 1)
        # test full stack
        full_stack = Stack(3, [1, 2, 3])
        self.assertEqual(full_stack.size(), 3)
        # test larger stack
        big_stack = Stack(30, [1] * 25)
        self.assertEqual(big_stack.size(), 25)


# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__':
    unittest.main()
