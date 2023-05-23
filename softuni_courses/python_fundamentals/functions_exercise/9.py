def between(a):
    counter = 0
    is_valid = True
    if not 6 <= len(a) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not a.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for i in a:
        if i.isnumeric():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


password = input()

between(password)
