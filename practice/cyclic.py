'''
Generate the first cyclic number.

'''


def isprime(p):
    if p > 1:
        for i in range(2,p // 2):
            if (p % i) == 0 :
                return False
        print("{} is a prime".format(p))
        return True
    else:
        return False


def iscyclic(num):
    digits = set(list(str(num)))
    print(digits)
    for n in range(2,7):
        comp = set(list(str(num * n)))
        print(num*n)
        if comp != digits:
            return False
    print("Got it!")
    return True


def cyclic_gen():
    print("Generate the first cyclic number!\n")
    n = 7
    if isprime(n):
        m =  (10**(n-1) -1) // n
        print(m)
        if iscyclic(m):
            print("{} is a cyclic number.".format(m))


if __name__ == '__main__':
    cyclic_gen()
