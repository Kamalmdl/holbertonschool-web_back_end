#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic caching system without limit"""

    def put(self, key, item):
        """Assign item to self.cache_data dictionary for the given key.
        Does nothing if key or item is None.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in self.cache_data.
        Returns None if key is None or key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]