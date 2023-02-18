import time


def fibonacci(n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


st = time.time()
print(fibonacci(30))
print(f"Execution time: {time.time() - st}")
