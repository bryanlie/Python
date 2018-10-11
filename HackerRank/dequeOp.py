'''

Perform append, pop, popleft and appendleft methods on an empty deque d.

'''

from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)

print(*[i for i in d])
