def sum_of_digit(n):
    assert n >= 0 and type(n) is int, "The numbers must be positive integer"
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digit(n//10)


print(sum_of_digit(999999999))
