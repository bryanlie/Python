'''
find Pythagorean triple (a, b, c) such that a^2 + b^2 = c^2
'''

import math


def sq_int(f):
    return int(math.sqrt(f))


def is_triple(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]

    arr.sort()

    for i in range(n-1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                print((sq_int(arr[j]), sq_int(arr[k]), sq_int(arr[i])))
                break
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            elif arr[j] + arr[k] > arr[i]:
                k -= 1


arr = [2, 11, 13, 15, 12, 17, 3, 5, 7, 9, 4]
arr_size = len(arr)

is_triple(arr, arr_size)
