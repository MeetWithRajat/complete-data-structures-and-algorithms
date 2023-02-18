def fibonacci(a, b, n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    if n > 0:
        print(a, end=" ")
        fibonacci(b, a+b, n-1)


fibonacci(5, 6, 10)
