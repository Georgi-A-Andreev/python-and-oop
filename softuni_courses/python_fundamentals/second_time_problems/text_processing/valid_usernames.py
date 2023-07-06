usernames = input().split(', ')

for el in usernames:
    valid = True
    if not 3 <= len(el) <= 16:
        valid = False
    for char in el:
        if not char.isdigit() and not char.isalpha() and char != '_' and char != '-':
            valid = False

    if valid:
        print(el)
