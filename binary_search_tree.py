from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return "TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right)


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None

    def search_helper(self, key, root):
        if root is None:
            return False
        if root.key == key:
            return True
        if root.key < key:
            return self.search_helper(key, root.right)
        if root.key > key:
            return self.search_helper(key, root.left)

    def search(self, key):  # returns True if key is in a node of the tree, else False
        return self.search_helper(key, self.root)

    def insert_helper(self, key, data, root):
        if root is None:
            root = TreeNode(key, data)
        else:
            if root.key == key:
                root.data = data
            elif root.key < key:
                root.right = self.insert_helper(key, data, root.right)
            else:
                root.left = self.insert_helper(key, data, root.left)
        return root

    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        self.root = self.insert_helper(key, data, self.root)

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.key, temp.data

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.key, temp.data

    def tree_height_helper(self, node):
        if node is None:
            return 0
        height = 1 + max(self.tree_height_helper(node.left), self.tree_height_helper(node.right))
        return height

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None
        return self.tree_height_helper(self.root) - 1

    def inorder_helper(self, root, pylist):
        if root:
            self.inorder_helper(root.left, pylist)
            pylist.append(root.key)
            self.inorder_helper(root.right, pylist)
        return pylist

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST
        return self.inorder_helper(self.root, [])

    def preorder_helper(self, root, pylist):
        if root:
            pylist.append(root.key)
            self.preorder_helper(root.left, pylist)
            self.preorder_helper(root.right, pylist)
        return pylist

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.preorder_helper(self.root, [])

    def level_order_helper(self, root, q: Queue, pylist):
        while root is not None:
            pylist.append(root.key)
            if root.left is not None:
                q.enqueue(root.left)
            if root.right is not None:
                q.enqueue(root.right)
            if not q.is_empty():
                root = q.dequeue()
            else:
                root = None
        return pylist

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        return self.level_order_helper(self.root, q, [])


# bst = BinarySearchTree()
# bst.insert(0, "Hello")
# bst.insert(3, "Hello")
# bst.insert(5, "Hello")
# bst.insert(2, "Goodbye")
# bst.insert(-4, "lowest")
# bst.insert(4, "lowest")
# print(bst.root)
# print(bst.find_min())
# print(bst.find_max())
# print(bst.tree_height())
# print(bst.inorder_list())
# print(bst.preorder_list())
# print(bst.level_order_list())
