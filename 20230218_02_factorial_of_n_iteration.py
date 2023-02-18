import time
import sys


sys.set_int_max_str_digits(0)


def factorial(n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


st = time.time()
print(factorial(100000))
print(f"Total execution time for iteration is {time.time() - st}")
