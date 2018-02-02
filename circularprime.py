'''
Generate the circular prime numbers with n digits.

'''


def is_prime(p):
    if p > 1:
        for i in range(2,p // 2):
            if (p % i) == 0 :
                return False
        return True
    else:
        return False


def is_circular(p):
    list_p = list(str(p))
    for i in range(3):
        list_p.insert(0, list_p.pop())
        if not is_prime(int(''.join(list_p))):
            return False
    return True


if __name__ == '__main__':
    for i in range(1111, 9999, 2):
        if is_prime(i) and is_circular(i):
            print(" {} is a circular prime with 4 digits.\n".format(i))