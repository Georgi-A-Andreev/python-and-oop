from math import floor


def func(a, b, c, d):

    point1.append(a)
    point1.append(b)

    point2.append(c)
    point2.append(d)

    if max(point1) > max(point2):
        return point2
    else:
        return point1


point1 = []
point2 = []
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

x = func(x1, y1, x2, y2)
print(f'({floor(x[0])}, {floor(x[1])})')
