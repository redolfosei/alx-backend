#!/usr/bin/python3
""" Module which implements basic dictionary
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ class BasicCache which Inherits from BaseCaching.
    """

    def put(self, key, item):
        """ Assigns the item value of key to self.cache_data dictionary.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data which is linked to the key.
        """
        return self.cache_data.get(key, None)
