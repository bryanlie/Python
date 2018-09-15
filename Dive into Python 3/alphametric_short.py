'''Find solutions to alphametic equations, short version without first letters.
e.g. 'SEND + MORE == MONEY')
'9567 + 1085 == 10652'
'''

import re
import itertools


def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    set_char = set(''.join(words))
    assert len(set_char) <= 10, 'Too many letters'
    char = tuple(ord(c) for c in set_char)
    digits = tuple(ord(c) for c in '0123456789')
    for guess in itertools.permutations(digits, len(char)):
       eq = puzzle.translate(dict(zip(char, guess)))
       if eval(eq):
          return eq


if __name__ == '__main__':
     print(solve('SEND + MORE == MONEY'))

