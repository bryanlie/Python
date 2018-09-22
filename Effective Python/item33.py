from pprint import pprint
import logging

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        pprint((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object, ):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print(Triangle.interior_angles())


try:
    print('Before class')
    class Line(Polygon):
        print('Before sides')
        sides = 1
        print('After sides')
    print('After class')
except:
    logging.exception('Expected')
else:
    assert False
