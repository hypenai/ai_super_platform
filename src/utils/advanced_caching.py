import functools
from cachetools import TTLCache, LRUCache

class HybridCache:
    def __init__(self, maxsize=1000, ttl=3600):
        self.ttl_cache = TTLCache(maxsize=maxsize, ttl=ttl)
        self.lru_cache = LRUCache(maxsize=maxsize)

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in self.ttl_cache:
                return self.ttl_cache[key]
            if key in self.lru_cache:
                return self.lru_cache[key]
            result = func(*args, **kwargs)
            self.ttl_cache[key] = result
            self.lru_cache[key] = result
            return result
        return wrapper

@HybridCache(maxsize=500, ttl=1800)
def compute_intensive_function(x, y):
    return x ** y

print("Advanced caching system online.")
