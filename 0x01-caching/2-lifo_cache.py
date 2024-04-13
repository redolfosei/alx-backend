#!/usr/bin/python3
""" Module with implements LIFO Caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Use self.cache_data - dictionary from the parent class
    BaseCaching
    """

    def __init__(self):
        """ class initializer Init
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Assigns the item value of the self.cache_data dictionary
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to the key in self.cache_data.
        """
        return self.cache_data.get(key, None)

    def is_full(self):
        """ Checks the lenght of  items in self.cache_data in relation to 
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ you must print DISCARD: with the key discarded and following by a
        new line -pop-
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
