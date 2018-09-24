a = '\x07'
print(repr(a))

b = eval(repr(a))
assert a == b

class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 2)
print(obj)


class BetterClass(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 2
    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)



obj = BetterClass(1, 2)
print(obj)

 
obj = OpaqueClass(4, 5)
print(obj.__dict__)