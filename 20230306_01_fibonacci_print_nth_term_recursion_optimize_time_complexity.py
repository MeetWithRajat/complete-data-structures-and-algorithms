import time


value_track = dict()


def fibonacci(n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_dynamic(n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    if n in [0, 1]:
        return n
    if n in value_track.keys():
        return value_track[n]
    else:
        value_track[n] = fibonacci_dynamic(n-1) + fibonacci_dynamic(n-2)
        return value_track[n]


# st = time.time()
# print(fibonacci(38))
# print(f"Execution time for normal approach: {time.time() - st}")

st = time.time()
print(fibonacci_dynamic(998))
print(f"Execution time for dynamic optimize approach: {time.time() - st}")
print(value_track)
