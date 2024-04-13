on3
""" Module for implementing MRU Caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """  MRUCache class that inherits from BaseCaching which is a caching
    system
    """

    def __init__(self):
        """ Initialization function 
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Assigns item value to the  self.cache_data library
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data which is linked to key.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)

    def is_full(self):
        """ Checks the lenght of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ print DISCARD: with the key discarded and following by a
        new line
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
