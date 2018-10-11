'''

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

'''

def palindromic(n):
    flag = False
    if len(str(n)) == 1:
        flag = True
    elif len(str(n)) % 2 == 1:
        a = list(str(n))
        for i in range(n // 2):
            flag = all(a[i] == a[-i])

    return flag


n = int(input())

arr = list(map(int, input().split()))

flag1 = all([i > 0 for i in arr])
flag2 = any(palindromic(i) for i in arr)

print(flag1 and flag2)
