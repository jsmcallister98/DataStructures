
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                  # empty heap

    def enqueue(self, item):
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if self.heap[len(self.heap) - 1] is not None:
            raise IndexError
        for i in range(1, len(self.heap)):
            if self.heap[i] is None:
                self.heap[i] = item
                self.num_items += 1
                break
        self.perc_up(self.num_items)

    def peek(self):
        """returns max without changing the heap
        Raises IndexError if the heap is empty"""
        if self.heap[1] == None:
            raise IndexError
        return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.num_items == 0:
            raise IndexError
        max_item = self.heap[1]
        i = 1
        while True:
            if i <= len(self.heap) - 1 and self.heap[i] is not None:
                i += 1
            else:
                break
        i -= 1
        self.heap[1] = self.heap[i]
        self.heap[i] = None
        self.num_items -= 1
        self.perc_down(1)
        return max_item

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        content_list = []
        for i in self.heap:
            if i is not None:
                content_list.append(i)
        return content_list

    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from 
        the items in alist using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        if len(alist) > len(self.heap) - 1:
            self.heap = [None] * (len(alist) + 1)
        else:
            self.heap = [None] * (len(self.heap))
        self.num_items = 0
        for i in range(len(alist)):
            self.heap[i + 1] = alist[i]
            self.num_items += 1
        for i in range(len(alist) // 2, 0, -1):
            self.perc_down(i)

    def is_empty(self):
        """returns True if the heap is empty, False otherwise"""
        return self.num_items == 0

    def is_full(self):
        """returns True if the heap is full, False otherwise"""
        return self.heap[len(self.heap) - 1] is not None
        
    def get_capacity(self):
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap) - 1
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items
        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.num_items:
            mc = self.maxChild(i)
            if self.heap[i] < self.heap[mc]:
                temp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = temp
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.num_items:
            return i * 2
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        for i in range(len(alist)):
            alist[i] = self.dequeue()
        alist.reverse()
        return alist
