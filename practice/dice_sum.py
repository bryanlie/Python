'''
5 dices (6,6,6,20,30) what's the probability of the sum bigger than 36 ?
'''

import random
import numpy as np

n = 3000
cnt = 0

for _ in range(n):
    a, b, c = np.random.randint(1, 7, 3)     #[low, high)
    d = random.randint(1, 20)           #[low, high]
    e = random.randint(1, 30)

    sum = a+b+c+d+e

    if sum > 36:
        cnt += 1

print("prop = {:.4}".format(cnt / n))
