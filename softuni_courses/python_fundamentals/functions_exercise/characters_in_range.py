def my_f(a1,b1):
    result = []
    for i in range(ord(a1) + 1, ord(b1)):
        result.append(chr(i))
    return result


a = input()
b = input()

print(' '.join(my_f(a, b)))
