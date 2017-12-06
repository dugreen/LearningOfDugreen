#!coding:utf-8

import time
from functools import wraps

n = 1000000

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper ( * args, ** kwargs):
        start = time.time()
        result = func( *args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n-=1

def main():
    countdown(n)

if __name__ == '__main__':
    main()
