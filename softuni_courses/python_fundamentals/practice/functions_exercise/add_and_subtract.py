def sum_numbers(first, second):
    return first + second


def subtract(aa, bb, cc):
    return sum_numbers(aa, bb) - cc


def add_and_subtract(aaa, bbb, ccc):
    return subtract(aaa, bbb, ccc)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
