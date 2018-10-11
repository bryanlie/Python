'''
Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''

n = int(input())
w = len("{0:b}".format(n))
for i in range(1,n+1):
  print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
