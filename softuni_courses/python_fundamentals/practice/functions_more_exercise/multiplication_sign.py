def multiplacation_sign(a, b, c):
    if 0 in (a, b, c):
        return 'zero'

    if len([i for i in [a, b, c] if abs(i) == i]) % 2 == 0:
        return 'negative'

    return 'positive'


a, b, c = int(input()), int(input()), int(input())

print(multiplacation_sign(a, b, c))
