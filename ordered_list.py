class Node:
    """Node for use with doubly-linked list"""

    def __init__(self, item, next=None, prev=None):
        self.item = item  # item held by Node
        self.next = next  # reference to next Node
        self.prev = prev  # reference to previous Node


class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""

    def __init__(self, sentinel=None):
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        """Returns back True if OrderedList is empty"""
        return self.sentinel == self.sentinel.next

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        cur = self.sentinel.next
        temp = Node(item)
        stop = False
        while cur.item is not None and not stop:
            if cur.item >= item:
                stop = True
                if cur.item == item:
                    return
            else:
                cur = cur.next
        temp.next = cur
        temp.prev = cur.prev
        cur.prev = temp
        temp.prev.next = temp

    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        cur = self.sentinel.next
        if self.is_empty():
            return False
        if cur.next.item is None:
            if cur.item == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = cur.next
                return True
            else:
                return False
        if cur.item == item:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            return True
        while cur.next.item is not None:
            if cur.item == item:
                break
            cur = cur.next
        if cur.next.item is not None:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            return True
        else:
            if cur.item == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            else:
                return False

    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        i = 0
        cur = self.sentinel.next
        while cur.item is not None:
            if cur.item == item:
                return i
            if cur.item > item:
                return None
            else:
                cur = cur.next
                i += 1

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        if 0 > index or index >= self.size() or self.is_empty():
            raise IndexError
        cur = self.sentinel.next
        while self.index(cur.item) <= index:
            if self.index(cur.item) == index:
                self.remove(cur.item)
                return cur.item
            else:
                cur = cur.next

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"""
        return self.search_helper(item, self.sentinel.next)

    def search_helper(self, item, current):
        cur = current
        while cur.item is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
                self.search_helper(cur.item, cur)
        return False

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        cur = self.sentinel.next
        pylist = []
        while cur != self.sentinel:
            pylist.append(cur.item)
            cur = cur.next
        return pylist

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        return self.reversed_helper(self.sentinel.next, [])

    def reversed_helper(self, current, pylist):
        cur = current
        if cur != self.sentinel:
            self.reversed_helper(cur.next, pylist).append(cur.item)
        return pylist

    def size(self):
        """Returns number of items in the OrderedList. O(n) is OK"""
        return self.size_helper(self.sentinel.next, 0)

    def size_helper(self, current, s):
        cur = current
        if cur != self.sentinel:
            s = self.size_helper(cur.next, s) + 1
        return s
