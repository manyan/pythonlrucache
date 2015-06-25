__author__ = 'xxmajia'


from lru.cache import LRUCache


def main():
    cache = LRUCache(3)
    print 'add hello -> world with ttl=60 into lru'
    cache.add_value('hello', 'world', ttl=3)
    print 'get value from cache: %s -> %s' % ('hello', cache.get_value('hello'))


if __name__ == "__main__":
    print __name__
    main()
