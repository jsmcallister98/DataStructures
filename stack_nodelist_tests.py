import unittest
from stack_nodelist import *


class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self):
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self):
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_is_empty(self):
        # test empty stack
        stack = Stack()
        self.assertTrue(stack.is_empty())
        # test non-empty stack
        stack1 = Stack(Node(1, None))
        self.assertFalse(stack1.is_empty())

    def test_push(self):
        # test push to empty list
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top, Node(1, None))
        # test additional push
        stack.push(2)
        self.assertEqual(stack.top, Node(2, Node(1, None)))

    def test_pop(self):
        # test empty list
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        # test normal pop
        stack_init = Node(3, Node(2, Node(1, None)))
        stack1 = Stack(stack_init)
        self.assertEqual(stack1.pop(), 3)
        self.assertEqual(stack1.top, Node(2, Node(1, None)))
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.top, Node(1, None))
        # test pop with one item in stack
        self.assertEqual(stack1.pop(), 1)
        self.assertEqual(stack1.top, None)

    def test_peek(self):
        # test empty stack
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
        # test normal peek
        stack_init = Node(3, Node(2, Node(1, None)))
        stack1 = Stack(stack_init)
        self.assertEqual(stack1.peek(), 3)
        self.assertEqual(stack1.top, Node(3, Node(2, Node(1, None))))
        # test peek with one item in stack
        stack2 = Stack(Node(1, None))
        self.assertEqual(stack2.peek(), 1)
        self.assertEqual(stack2.top, Node(1, None))

    def test_size(self):
        # test empty stack
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        # test non-empty stack
        stack1 = Stack(Node(1, Node(2, None)))
        self.assertEqual(stack1.size(), 2)
        # test after push
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        # test after pop
        stack.pop()
        self.assertEqual(stack.size(), 0)


# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__':
    unittest.main()
