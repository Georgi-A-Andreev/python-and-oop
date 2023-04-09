def even_odd(*args):
    command = args[-1]
    result = []

    for i in args[:-1]:
        if i % 2 == 0 and command == 'even':
            result.append(i)
        if i % 2 == 1 and command == 'odd':
            result.append(i)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))