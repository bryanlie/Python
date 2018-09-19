import logging

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
evens = a[::2]
odds = a[1::2]

print(evens)
print(odds)

x = b'mongoose'
y = x[::-1]
print(y)

try:
    w = '谢谢'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except:
    logging.exception('Expected')
else:
    assert False

print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])

b = a[::2]
c = b[1:-1]
print(b)
print(c)