'''
3 dice, probability of strictly decreasing ?
'''

import numpy as np

n = 1000000
cnt = 0

for _ in range(n):
    a, b, c = np.random.randint(1, 7, 3)

    if (a > b) and (b > c):
        cnt += 1

print(cnt / n)
print(5 / 54)
