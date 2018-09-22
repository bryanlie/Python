from pprint import pprint


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        super(TimesFive, self).__init__(value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        super(PlusTwo, self).__init__(value)
        self.value += 2


class GoodWay(TimesFive, PlusTwo):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


pprint(GoodWay.mro())  #MRO（Method Resolution Order）
foo = GoodWay(5)
print("Should be 5 * (5 + 2) = 35 and is " , foo.value)

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value