__author__ = 'xxmajia'

import unittest
from lru.cache import LRUCache
from time import sleep


class TestLRU(unittest.TestCase):
    def setUp(self):
        """set up: init a LRUCache"""
        self.cache = LRUCache(3)

    def test_lru_basic(self):
        test_value = [0, 1, 2, 3, 4]
        expected_value = [2, 3, 4]
        removed_value = [0, 1]
        for i in test_value:
            self.cache.add_value(i, i)

        for i in expected_value:
            self.assertEqual(self.cache.get_value(i), i)

        for i in removed_value:
            self.assertEqual(self.cache.get_value(i), None)

    def test_ttl(self):
        cache = LRUCache(3)
        cache.add_value('hello', 'world', ttl=3)
        self.assertEqual(cache.get_value('hello'), 'world')
        sleep(5)
        self.assertEqual(cache.get_value('hello'), None)

    def tearDown(self):
        """Cleaning up after the test"""


if __name__ == '__main__':
    unittest.main()