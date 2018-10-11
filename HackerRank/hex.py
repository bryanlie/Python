'''
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

1. It must start with a '#' symbol.
2. It can have 3 or 6  digits.
3. Each digit is in the range of 0 to F. 
4. letters can be lower case

'''

import re

n = int(input())

for _ in range(n):
    line = input()
    e = re.findall(r'[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s;,)]', line, re.I)
    for i in e:
        print(i)
