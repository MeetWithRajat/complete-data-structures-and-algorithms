def power(a, b):
    assert type(b) is int, "The numbers b must be integer"
    if b == 0:
        return 1
    elif b < 0:
        return 1/a * power(a, b+1)
    else:
        return a * power(a, b-1)


print(power(2, 5))
