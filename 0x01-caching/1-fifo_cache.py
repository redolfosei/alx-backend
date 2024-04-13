#!/usr/bin/python3
""" Module which implements FIFO caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ class inherits from BaseCaching which is a caching system
    """

    def __init__(self):
        """ Initializer function the class FIFOCache
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Assigns the item value of key to the self.cache_data dictionary.
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
        """ Checks lenght of items in self.cache_data in relation to 
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ function outputs discarded items
        """
        popped = self.queue.popleft()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
