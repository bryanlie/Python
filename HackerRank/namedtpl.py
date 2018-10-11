'''
Dr. John Wesley has a spreadsheet containing a list of student's id, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.
'''

from collections import namedtuple

n = int(input())
fields_names = input().split()
Student = namedtuple('Student', fields_names)

sum = 0
for _ in range(n):
    a = input().split()
    std = Student(*a)
    sum += int(std.MARKS)

print('%0.2f' % (sum / n))
