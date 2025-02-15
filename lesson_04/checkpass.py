def check_password(password):
    if len(password) < 8:
        return False

    has_digit = has_upper = has_lower = False

    for char in password:
        if '0' <= char <= '9':
            has_digit = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True

    return has_digit and has_upper and has_lower


print(check_password("Abc12345"))
print(check_password("abc12345"))
print(check_password("ABC12345"))
print(check_password("abcABC12"))
