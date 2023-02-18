import time
import sys


sys.set_int_max_str_digits(0)
sys.setrecursionlimit(100050)


def factorial(n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    if n == 0:
        return 1
    return n * factorial(n-1)


st = time.time()
print(factorial(100000))
print(f"Total execution time for recursion is {time.time() - st}")
