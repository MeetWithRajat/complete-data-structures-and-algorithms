def is_palindrome(st):
    if st[0] == st[-1]:
        if len(st) <= 2:
            return True
        else:
            return is_palindrome(st[1:-1])
    return False


print(is_palindrome("advda"))
