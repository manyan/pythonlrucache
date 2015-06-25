__author__ = 'xxmajia'

"""
this file holds a singleton of lru cache, add ttl mechanism to the original one
Usage:
As its a app-level cache, we should only keep a copy of this in a process
"""

import pylru
import time


class CacheItem():
    """
    CacheItem is meant for internal use only, just wrapping the ttl inside
    """
    def __init__(self, value, ttl=5*60):
        """
        :param value: is the value that we wanna cache
        :param ttl: ttl in seconds, should set ttl to avg use time
        :return:
        """
        self.value = value
        # convert ttl to unix timestamp for easier comparison
        self.valid_until = int(time.time()) + ttl

    def get_value(self):
        return self.value

    def is_expired(self):
        return int(time.time()) > self.valid_until


class LRUCache():
    """
    This class will just hold an instance of pylru.cache, and adding TTL param to auto delete the cache when expires
    """
    def __init__(self, size=10):
        """
        :param size: int, size of the cache, should match the actual concurrent users,
                    as we should only assign one key-value for one user
        :return:
        """
        self.cache = pylru.lrucache(size)
        self.size = size

    def get_value(self, key):
        # cache.get(key) will return a value or None, without throwing exception
        item = self.cache.get(key)

        if item and (not isinstance(item, CacheItem) or item.is_expired()):
            del self.cache[key]
            return None

        return item.get_value() if item else None

    def remove_expires(self):
        for key in self.cache:
            self.get_value(key)

    def add_value(self, key, value, ttl=5*60):
        item = CacheItem(value, ttl)
        self.cache[key] = item

    def get_current_size(self):
        return len(self.cache)

    def get_max_size(self):
        return self.size

    def health_check(self):
        try:
            self.add_value('health_check', 'OK', 5)
            status = self.get_value('health_check') == 'OK'
            self.remove_expires()
            return status
        except Exception:
            return False

    def get_cache_status(self, full_status=False):
        self.remove_expires()
        msg = 'Max size: %s, actual size: %s. \r\n' % (self.get_max_size(), self.get_current_size())
        if full_status:
            key_value_paris = {}
            for k in self.cache:
                key_value_paris[k] = self.get_value(k)
            msg += ' Contents: %s' % key_value_paris

        return msg