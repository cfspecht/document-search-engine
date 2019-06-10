""" Lab 7: Implementing Hash Tables with Different Collision Resolutions
Chris Specht
CPE 202-09
Spring 2019
"""


from linked_list import LinkedList


class HashTableSepchain:
    """ Hash table implementation using separate chaining for collision resolution
    Attributes:
        table (list): the hash table in Python list format, stores LLNodes of tuples of (key, data)
        table_size (int): number of slots in table
        num_items (int): number of items in hash table
        num_collisions (int): number of collisions that have occured during insertions
    """
    def __init__(self, table_size=11):
        self.table = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.num_collisions = 0

    def __repr__(self):
        return "HashTableSC {table size: %s, items: %s, collisions: %s, %s}" % (self.table_size,
                                                                                self.num_items,
                                                                                self.num_collisions,
                                                                                self.table)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.table == other.table and \
               self.table_size == other.table_size and \
               self.num_items == other.num_items and \
               self.num_collisions == other.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """ Inserts a key-item pair into hash table based on hash_value of the key. If a key already
        exists, the item will be overriden. If the insertion would increase the load factor beyond
        1.5, table is re-hashed and then item is inserted
        Args:
            key (str): key of item
            data (any): item to be inserted
        """
        #if inserting disrupts load factor (1.5 for separate chaining)
        potential_load_factor = (self.num_items + 1) / self.table_size
        if potential_load_factor > 1.5:
            self.rehash()

        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # if key already exists, override the data
        if self.table[hash_value] != None and self.table[hash_value].search(key):
            self.table[hash_value].replace(key, data) # self.table[hash_value] is a LinkedList

        # if desired slot is empty
        elif self.table[hash_value] is None:
            # store every key, data pair inside a linked list
            linked_list = LinkedList()
            linked_list.insert(key, data)
            self.table[hash_value] = linked_list

        # if desired slot is full but not of same object, use separate chaining
        else:
            self.table[hash_value].insert(key, data)
            self.num_collisions += 1


        self.num_items += 1

    def rehash(self):
        """ Resizes table so that more items can be inserted, as well as takes old items from table
            and re-inserts them into new table
        """
        # create new, bigger hash table
        old_table = self.table
        new_size = 2 * self.table_size + 1
        new_table = [None] * new_size
        self.table = new_table     # updates table attribute to larger, empty table
        self.table_size = new_size # updates table_size attribute
        self.num_items = 0         # updates number of items in current table to 0

        # insert old table's items into new_table
        # iterate through linked lists in table
        for linked_list in old_table:

            # if there is a linked list in slot, take value and add it to new table
            if linked_list is not None:

                # pop every node in current linked list until it is empty
                # insert that key-value pair back into new hash_table
                while linked_list.head is not None:
                    popped_tuple = linked_list.pop()
                    self.put(popped_tuple[0], popped_tuple[1])

    def get(self, key):
        """ Takes a key and returns the key-value pair from the hash table associated with the key
        Args:
            key (str): key of target item
        Returns:
            (key, any): key-value pair
        Raises:
            KeyError: if key is not found
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # if no key-item pair associated with key, raise error
        if self.table[hash_value] is None or not self.table[hash_value].search(key):
            raise LookupError("Key is not found in table")

        # return tuple of key-item pair
        return (key, self.table[hash_value].get(key))

    def contains(self, key):
        """ Returns True if the key exists in the table, otherwise returns False
        Args:
            key (str): key of target item
        Returns:
            bool: whether key exists in hash table or not
        """
        # calculate hash of key
        hash_value = hash_string(key, self.table_size)
        # call search function
        return self.table[hash_value].search(key)

    def remove(self, key):
        """ Takes a key, removes the key-item pair from the hash table and returns the key-item pair
        Args:
            key (str): key of target item
        Returns:
            (key, item): tuple of key and item
        Raises:
            LookupError: if key does not exist
        """
        # check if target pair exists
        if not self.contains(key):
            raise LookupError("No key-item pair associated with key")

        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # remove node and return target key-value pair
        result = self.table[hash_value].remove(key)
        result_pair = (result.key, result.data)

        # if linkedlist is empty after removal, set slot to None
        if self.table[hash_value].is_empty():
            self.table[hash_value] = None

        # decrement num_item by 1
        self.num_items -= 1

        # return target pair
        return result_pair

    def size(self):
        """ Returns number of key-value pairs currently stored in table
        Returns:
            int: number of key-value pairs
        """
        return self.num_items

    def load_factor(self):
        """ Returns current load factor of the table
        Returns:
            float: load factor of table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """ Returns cumulative number of collisions that have occured
        Returns:
            int: number of collisions
        """
        return self.num_collisions


class HashTableLinear:
    """ Hash table implementation using Linear Probing as collision resolution
    Attributes:
        table (list): hash table in Python list format, stores (key, data)
        table_size (int): size of table
        num_items (int): number of items
        num_collisions (int): cumulative number of collisions that have happened during insertion
    """
    def __init__(self, table_size=11):
        self.table = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.num_collisions = 0

    def __repr__(self):
        return "HashTableL {table size: %s, items: %s, collisions: %s, %s}" % (self.table_size,
                                                                               self.num_items,
                                                                               self.num_collisions,
                                                                               self.table)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.table == other.table and \
               self.table_size == other.table_size and \
               self.num_items == other.num_items and \
               self.num_collisions == other.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """ Inserts a key-item pair into a hash table based on key's hash value. If key-data pair
        being inserted is a duplicate, override key-data pair. If insertion will cause load factor
        to rise above 0.75, resize the table then insert.
        Args:
            key (str): key to be inserted
            data (any): data to be inserted
        """
        # if inserting disrupts load factor (0.75), resize table
        potential_load_factor = (self.num_items + 1) / self.table_size
        if potential_load_factor > 0.75:
            self.resize_table()

        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # starting at initial hash value, iterate until matching key or open slot is found
        # loop will break when either open slot or correct slot is reached
        while self.table[hash_value] != None and self.table[hash_value][0] != key:
            hash_value = self.rehash_string(hash_value)
            self.num_collisions += 1

        # set current slot to key-data pair
        self.table[hash_value] = (key, data)

        # update number of items
        self.num_items += 1

    def resize_table(self):
        """ Resizes the hash table, helper to the put() method, works for linear & quadratic probing
        """
        # create new, bigger hash table
        old_table = self.table
        new_size = 2 * self.table_size + 1
        new_table = [None] * new_size
        self.table = new_table     # updates table attribute to larger, empty table
        self.table_size = new_size # updates table_size attribute
        self.num_items = 0         # updates number of items in current table to 0
        # iterate through slots in table
        for slot in old_table:
            # if there is a tuple in slot
            if slot is not None:
                # insert key-value pair into new_hash table
                self.put(slot[0], slot[1])

    def rehash_string(self, hash_value):
        """ Rehashes the hash_value for linear probing
        Args:
            hash_value (int): hash value to be rehashed
        Returns:
            int: new rehashed value
        """
        return (hash_value + 1) % self.table_size

    def get(self, key):
        """ Takes a key and returns the key-item pair associated with the key
        Args:
            key (str): target key
        Returns:
            (key, item): target key-item pair
        Raises:
            LookupError: No key-item pair is associated with the key
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # loop will break when either open slot or correct slot is reached
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_string(hash_value)

        # if empty slot is reached
        if self.table[hash_value] is None:
            raise LookupError("No key-item pair is associated with the key")

        # if correct slot is reached
        return self.table[hash_value]

    def contains(self, key):
        """ Returns True if the key exists in the table, otherwise returns False
        Args:
            key (str): key of target item
        Returns:
            bool: whether key exists in hash table or not
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # loop will break when either open slot or correct slot is reached
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_string(hash_value)

        # if empty slot is reached
        if self.table[hash_value] is None:
            return False

        # if key-item pair is found
        return True

    def remove(self, key):
        """ Takes a key, removes the key-item pair from the hash table and returns the key-item pair
        Args:
            key (str): key of target item
        Returns:
            (key, item): tuple of key and item
        Raises:
            LookupError: if key does not exist
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # loop will break when either open slot or correct slot is reached
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_string(hash_value)

        # if empty slot is reached
        if self.table[hash_value] is None:
            raise LookupError("No key-item pair is associated with the key")

        # else stores the target item and deletes it
        target_pair = self.table[hash_value]
        self.table[hash_value] = None

        # create new hash table
        old_table = self.table
        new_table = [None] * self.table_size
        self.table = new_table     # updates table attribute to new empty table
        self.num_items = 0         # updates number of items in current table to 0
        # iterate through slots in table
        for slot in old_table:
            # if there is a tuple in slot
            if slot is not None:
                # insert key-value pair into new_hash table
                self.put(slot[0], slot[1])

        # return removed tuple
        return target_pair

    def size(self):
        """ Returns the number of items in the hash table
        Returns:
            int: number of items
        """
        return self.num_items

    def load_factor(self):
        """ Returns current load factor of the table
        Returns:
            float: load factor of table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """ Returns cumulative number of collisions that have occured
        Returns:
            int: number of collisions
        """
        return self.num_collisions

    def keys(self):
        """ Returns a list of keys in the hash table, necessary for Proj4: Document Search Engine
        Returns:
            list: list of keys
        """
        return [atuple[0] for atuple in self.table if atuple]


class HashTableQuadratic:
    """ Hash table implementation using Quadratic Probing as collision resolution
    Attributes:
        table (list): hash table in Python list format
        table_size (int): size of table
        num_items (int): number of items
        num_collisions (int): cumulative number of collisions that have happened during insertion
    """
    def __init__(self, table_size=11):
        self.table = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.num_collisions = 0

    def __repr__(self):
        return "HashTableQ {table size: %s, items: %s, collisions: %s, %s}" % (self.table_size,
                                                                               self.num_items,
                                                                               self.num_collisions,
                                                                               self.table)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.table == other.table and \
               self.table_size == other.table_size and \
               self.num_items == other.num_items and \
               self.num_collisions == other.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """ Inserts a key-item pair into a hash table based on key's hash value. If key-data pair
        being inserted is a duplicate, override key-data pair. If insertion will cause load factor
        to rise above 0.75, resize the table then insert.
        Args:
            key (str): key to be inserted
            data (any): data to be inserted
        """
        # if inserting disrupts load factor (0.75), resize table
        potential_load_factor = (self.num_items + 1) / self.table_size
        if potential_load_factor > 0.75:
            self.resize_table()

        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # starting at initial hash value, iterate until matching key or open slot is found
        # loop will break when either open slot or correct slot is reached
        # quadratic probing
        i = 1
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_quadratic(hash_value, i)
            # if correct slot is found, breaks loop before value is rehashed
            if self.table[hash_value] is not None and self.table[hash_value][0] == key:
                break
            i += 1
            self.num_collisions += 1

        # set current slot to key-data pair
        self.table[hash_value] = (key, data)

        # update number of items
        self.num_items += 1

    def resize_table(self):
        """ Resizes the hash table, helper to the put() method, works for linear & quadratic probing
        """
        # create new, bigger hash table
        old_table = self.table
        new_size = 2 * self.table_size + 1
        new_table = [None] * new_size
        self.table = new_table     # updates table attribute to larger, empty table
        self.table_size = new_size # updates table_size attribute
        self.num_items = 0         # updates number of items in current table to 0
        # iterate through slots in table
        for slot in old_table:
            # if there is a tuple in slot
            if slot is not None:
                # insert key-value pair into new_hash table
                self.put(slot[0], slot[1])

    def rehash_quadratic(self, hash_value, i):
        """ Rehashes the hash value according to quadratic probing. i should be 1, 2, 3, ...
        Args:
            hash_value (int): hash value to be rehashed
            i (int): current increment of quadratic probing
        Returns:
            int: new hash value
        """
        return (hash_value + (i ** 2)) % self.table_size


    def get(self, key):
        """ Takes a key and returns the key-item pair associated with the key
        Args:
            key (str): target key
        Returns:
            (key, item): target key-item pair
        Raises:
            LookupError: No key-item pair is associated with the key
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # quadratic probing
        i = 1
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_quadratic(hash_value, i)
            # if correct slot is found, breaks loop before value is rehashed
            if self.table[hash_value] is not None and self.table[hash_value][0] == key:
                break
            i += 1
            self.num_collisions += 1

        # if empty slot is reached
        if self.table[hash_value] is None:
            raise LookupError("No key-item pair is associated with the key")

        # if correct slot is reached
        return self.table[hash_value]

    def contains(self, key):
        """ Returns True if the key exists in the table, otherwise returns False
        Args:
            key (str): key of target item
        Returns:
            bool: whether key exists in hash table or not
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # quadratic probing
        i = 1
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_quadratic(hash_value, i)
            # if correct slot is found, breaks loop before value is rehashed
            if self.table[hash_value] is not None and self.table[hash_value][0] == key:
                break
            i += 1
            self.num_collisions += 1

        # if empty slot is reached
        if self.table[hash_value] is None:
            return False

        # if key-item pair is found
        return True


    def remove(self, key):
        """ Takes a key, removes the key-item pair from the hash table and returns the key-item pair
        Args:
            key (str): key of target item
        Returns:
            (key, item): tuple of key and item
        Raises:
            LookupError: if key does not exist
        """
        # calculate hash value
        hash_value = hash_string(key, self.table_size)

        # quadratic probing
        i = 1
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = self.rehash_quadratic(hash_value, i)
            # if correct slot is found, breaks loop before value is rehashed
            if self.table[hash_value] is not None and self.table[hash_value][0] == key:
                break
            i += 1
            self.num_collisions += 1

        # if empty slot is reached
        if self.table[hash_value] is None:
            raise LookupError("No key-item pair is associated with the key")

        # else stores the target item and deletes it
        target_pair = self.table[hash_value]
        self.table[hash_value] = None

        # create new hash table
        old_table = self.table
        new_table = [None] * self.table_size
        self.table = new_table     # updates table attribute to new empty table
        self.num_items = 0         # updates number of items in current table to 0
        # iterate through slots in table
        for slot in old_table:
            # if there is a tuple in slot
            if slot is not None:
                # insert key-value pair into new_hash table
                self.put(slot[0], slot[1])

        # return removed tuple
        return target_pair

    def size(self):
        """ Returns the number of items in the hash table
        Returns:
            int: number of items
        """
        return self.num_items

    def load_factor(self):
        """ Returns current load factor of the table
        Returns:
            float: load factor of table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """ Returns cumulative number of collisions that have occured
        Returns:
            int: number of collisions
        """
        return self.num_collisions


def hash_string(string, size):
    """ Returns the hash index of a string
    Args:
        string (str): string to be hashed
        size (int): size of the hash table
    Returns:
        int: resulting hash of the string
    """
    hash_result = 0
    for char in string:
        hash_result = (hash_result * 31 + ord(char)) % size
    return hash_result


def import_stopwords(filename, hashtable):
    """ Import stop words from text file and turn it into a HashTable object
    Args:
        filename (str): name of the file containing stopwords
        hashtable (HashTable): hash table object of Sepchain/Linear/Quadratic
    Returns:
        HashTable: hash table object containing stopwords
    """
    # open filename with python builtin open() function
    file_pointer = open(filename, "r")
    raw_words = file_pointer.readlines()
    word_list = raw_words[0].split(" ")
    file_pointer.close()

    # iterate through stop words ["word1", "word2", ...]
    for stop_word in word_list:

        # put each stop word into hash table
        hashtable.put(stop_word, stop_word)

    # return created hash table object
    return hashtable
