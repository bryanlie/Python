'''
 A drunkard begins walking aimlessly, starting at a lamp post. 
 At each time step he takes one step at random, either north, east, south, or west.
 How far will the drunkard be from the lamp post after N steps? 
'''

import numpy as np


def randomWalk(steps):
    x, y = 0, 0
    directions = ('E', 'W', 'N', 'S')
    for _ in range(steps):
        a = np.random.choice(directions)
        if a == 'E':
            x += 1
        elif a == 'W':
            x -= 1
        elif a == 'N':
            y += 1
        elif a == 'S':
            y -= 1
    print("(x, y) = ({}, {})".format(x, y))

randomWalk(20)
