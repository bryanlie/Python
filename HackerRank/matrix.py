'''

Neo has a complex matrix script. The matrix script is a n X m  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).


e.g. input

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

The decoded script is:
This$#is% Matrix#  %!

'''

import re


nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

a = []
for i in range(m):
    for line in matrix:
        a.append(line[i])
arr = ''.join(a)

print(re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', arr))
