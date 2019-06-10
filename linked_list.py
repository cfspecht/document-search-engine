""" Lab 3: Linked List Implementation for Hash Table Separate Chaining
Chris Specht
CPE 202-09
Spring 2019
"""


class LinkedList:
    """ Linked List wrapper class
    Attributes:
        head (Node/NoneType): head/front of the linked list
    """
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return "LinkL{%s}" % (self.head)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.head == other.head

    def is_empty(self):
        """ Checks if linked list is empty
        """
        return self.head is None

    def insert(self, key, item):
        """ Inserts a key-value pair into Node into linked list
        Args:
            key (str): key of object
            item (any): data to be inserted
        """
        temp = Node(key, item)
        temp.set_next(self.head)
        self.head = temp

    def replace(self, key, new_item):
        """ Replaces the data of an existing node given a key
        Args:
            key (str): key of object
            new_item (any): new data to override old one
        Raises:
            IndexError: target key does not exist
        """
        if not self.search(key):
            raise IndexError("Object with given key does not exist")
        current = self.head
        found = False
        while not found:
            if current.get_key() == key:
                found = True
            else:
                current = current.get_next()
        current.set_data(new_item)

    def remove(self, key):
        """ Given key, removes associated Node
        Args:
            key (any): key of Node to be removed
        Returns:
            Node: the removed node
        Raises:
            IndexError: target key does not exist
        """
        if not self.search(key):
            raise IndexError("Object with given key does not exist")
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_key() == key:
                found = True
            else:
                previous = current
                current = current.get_next()
        target_node = current
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return target_node

    def pop(self):
        """ Removes head node and returns its data in a tuple
        Returns:
            (str, any): (key, value) tuple
        """
        # key-value pair to be returned
        target_pair = (self.head.key, self.head.data)
        # removes node from linked list
        self.head = self.head.get_next()
        return target_pair

    def get(self, key):
        """ Returns data associated with a key
        Args:
            key (str): key of data to be retrieved
        Returns:
            any: target data
        """
        current = self.head
        found = False
        while not found:
            if current.get_key() == key:
                found = True
            else:
                current = current.get_next()
        return current.get_data()

    def search(self, key):
        """ Returns boolean of whether an item has an associated Node in the linked list
        Args:
            item (any): data of target node to search for
        Returns:
            bool: True if found, else False
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.get_key() == key:
                found = True
            else:
                current = current.get_next()
        return found


class Node:
    """ Node for a linked list that stores a key-value pair
    Attributes:
        key (str): key for data
        data (any): data to be stored
        next (Node/NoneType): next node in list
    """
    def __init__(self, key, data, next_node=None):
        self.key = key
        self.data = data
        self.next = next_node

    def __eq__(self, other):
        return (isinstance(other, Node) and
                self.key == other.key and
                self.data == other.data and
                self.next == other.next)

    def __repr__(self):
        return "Node(%s, %s, %s)" % (self.key, self.data, self.next)

    def get_key(self):
        """ Retrieves key stored in node
        Returns:
            str: key of the node
        """
        return self.key

    def get_data(self):
        """ Retrieves data stored in node
        Returns:
            self.data (any): data stored in node
        """
        return self.data

    def get_next(self):
        """ Retrieves the next node
        Returns:
            self.next (Node): next node in list
        """
        return self.next

    def set_data(self, new_data):
        """ Overwrites data in the node
        Args:
            new_data (any): data to be stored
        """
        self.data = new_data

    def set_next(self, new_next):
        """ Overwrites callee node's next node
        Args:
            new_next (Node): node to be linked to callee node
        """
        self.next = new_next
