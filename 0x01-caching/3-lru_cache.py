#!/usr/bin/python3
""" Module for impl3m3nting LRU Caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ Create a class LRUCache that inherits from BaseCaching and is a caching
    system
    """

    def __init__(self):
        """ Init
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Assigns to the dictionary self.cache_data the item value fo
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)

    def is_full(self):
        """ Checks the lenght of items in self.cache_data in relation to 
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ you must print DISCARD: with the key discarded and following by a
        new line
        """
        popped = self.queue.popleft()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
