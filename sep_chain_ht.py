
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, value):
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if key < 0:
            raise ValueError

        hash_value = key % self.table_size

        if not self.hash_table[hash_value]:
            self.hash_table[hash_value].append((key, value))
            self.num_items += 1
            return

        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                self.hash_table[hash_value][i] = (key, value)
                return

        self.hash_table[hash_value].append((key, value))
        self.num_items += 1
        self.num_collisions += 1

        # check load factor
        if self.num_items >= self.table_size * 1.5:
            self.num_items = 0
            collisions = self.num_collisions
            old_hash_table = self.hash_table
            size = self.table_size * 2 + 1
            self.hash_table = [[] for _ in range(size)]
            self.table_size = size

            for sub_list in old_hash_table:
                for key_value in sub_list:
                    self.insert(key_value[0], key_value[1])

            self.num_collisions = collisions

    def get_item(self, key):
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        for sub_list in self.hash_table:
            for key_value in sub_list:
                if key_value[0] == key:
                    return key_value[1]

        raise LookupError

    def remove(self, key):
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        for sub_list in range(len(self.hash_table)):
            for key_value in range(len(self.hash_table[sub_list])):
                if self.hash_table[sub_list][key_value][0] == key:
                    self.num_items -= 1
                    return self.hash_table[sub_list].pop(key_value)

        raise LookupError

    def load_factor(self):
        """Returns the current load factor of the hash table"""
        return self.num_items / self.table_size

    def size(self):
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self):
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions
