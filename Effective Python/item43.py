import logging
from threading import Lock


lock = Lock()
with lock:
    print('Lock is held')


lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()


logging.getLogger().setLevel(logging.WARNING)
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')

my_function()

from contextlib import contextmanager
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
    print('Inside:')
    my_function()
print('After:')
my_function()


with open('my_output.txt', 'w') as handle:
    handle.write('This is some data!')


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('THis is my message!')
    logging.debug('This will not print')


logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
