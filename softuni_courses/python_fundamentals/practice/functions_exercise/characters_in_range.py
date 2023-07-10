def ascii_range(begin, end):
    result = []
    for i in range(ord(begin) + 1, ord(end)):
        result.append(chr(i))

    return ' '.join(result)


first = input()
second = input()

print(ascii_range(first, second))
