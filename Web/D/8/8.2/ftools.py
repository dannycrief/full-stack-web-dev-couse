import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


@lru_cache
def fibo_steroids(n):
    if n in [0, 1]:
        return n
    else:
        return fibo_steroids(n - 1) + fibo_steroids(n - 2)


print(fibo_steroids(2049))
