def validator(password):
    errors = ''

    if not 6 <= len(password) <= 10:
        errors += "Password must be between 6 and 10 characters"

    for l in password:
        if not l.isdigit() and not l.isalpha():
            errors += "\nPassword must consist only of letters and digits"
            break

    counter = 0
    for el in password:
        if el.isdigit():
            counter += 1

    if counter < 2:
        errors += "\nPassword must have at least 2 digits"

    if errors == '':
        return "Password is valid"

    return errors


input_password = input()

print(validator(input_password))
