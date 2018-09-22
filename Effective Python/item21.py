import logging

def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)
assert result is 0

result = safe_division(1.0, 0, False, True)
print(result)
assert result == float('inf')


def safe_division_b(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


assert safe_division_b(1.0, 10**500, ignore_overflow=True) is 0
assert safe_division_b(1.0, 0, ignore_zero_division=True) == float('inf')


def safe_division_c(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


try:
    safe_division_c(1.0, 10**500, True, False)
except:
    logging.exception('Expected')
else:
    assert False


print(safe_division_c(1.0, 0, ignore_zero_division=True))
try:
    print(safe_division_c(1.0, 0))
    assert False
except ZeroDivisionError:
    pass