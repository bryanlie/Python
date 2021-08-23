'''
coupon collector's problem
'''

import random
import numpy as np

n = 6
N = 3000
a = []

for _ in range(N):
    s = set()
    cnt = 0

    while len(s) < n:
        i = random.randint(1, n)
        s.add(i)
        cnt += 1

    a.append(cnt)


print(np.mean(a))