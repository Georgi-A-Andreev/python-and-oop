def sum_numbers(a1,b1):
    return a1 + b1


def my_f(a2,b2,c2):
    return sum_numbers(a2, b2) - c2


a = int(input())
b = int(input())
c = int(input())

print(my_f(a, b, c))
