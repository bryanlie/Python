import logging

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]

print(a[:4])
print(a[-4:])
print(a[3:-3])

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

print(a[:20])
print(a[-20:])

try:
    print(a[20])
except:
    logging.exception('Expected!')
else:
    assert False

b = a[4:]
print('Before:  ', b)
b[1] = 99
print('After:   ', b)

print('Before   ', a)
a[2:7] = [88, 28, 18]
print('After    ', a)

b = a[:]
assert b == a and b is not a

b = a
print('Before   ', a)
a[:] = [101, 102, 103]
assert a is b
print('After    ', a)
