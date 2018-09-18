import os
import logging

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_str(b'foo')))
print(repr(to_str('foo')))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('foo')))


try:
    with open('random.bin', 'w') as f:
        f.write(os.urandom(10))
except:
    logging.exception('Expected')
else:
    assert False


with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
