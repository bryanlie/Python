import logging


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace
def fibonacci(n):
    if n in (0,1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci = trace(fibonacci)
fibonacci(3)
print(fibonacci)

try:
    import pickle

    def my_func():
        return 1

    print(pickle.dumps(my_func))

    @trace
    def my_func2():
        return 2

    print(pickle.dumps(my_func2))
except:
    logging.exception('Expected')
else:
    assert False

help(fibonacci)

from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n -1))

help(fibonacci)