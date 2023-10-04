def even_odd(*args):
    if args[-1] == 'even':
        return [el for el in args[:len(args) - 1] if el % 2 == 0]
    return [el for el in args[:len(args) - 1] if el % 2 != 0]



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
