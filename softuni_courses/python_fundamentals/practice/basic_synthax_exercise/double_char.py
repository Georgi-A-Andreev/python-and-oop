while True:
    text = input()
    if text == 'End':
        break

    if text == 'SoftUni':
        continue

    for i in text:
        print(2 * i, end='')

    print()
