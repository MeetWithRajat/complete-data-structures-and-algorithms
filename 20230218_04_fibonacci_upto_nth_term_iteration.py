def fibonacci(a, b, n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b


fibonacci(5, 6, 10)
