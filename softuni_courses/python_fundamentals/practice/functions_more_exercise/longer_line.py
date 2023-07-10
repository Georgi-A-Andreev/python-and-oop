from math import sqrt


def closest_point(one, two):
    if max([abs(i) for i in one]) <= max([abs(i) for i in two]):
        return f'{(int(one[0]), int(one[1]))}{(int(two[0]), int(two[1]))}'

    return f'{(int(two[0]), int(two[1]))}{(int(one[0]), int(one[1]))}'


def distance_from_origin(x, y):
    return sqrt(x**2 + y**2)


def longest_line(one, two, three, four):
    point_one_length = distance_from_origin(one[0], one[1]) + distance_from_origin(two[0], two[1])
    point_two_length = distance_from_origin(three[0], three[1]) + distance_from_origin(four[0], four[1])

    if point_one_length >= point_two_length:
        return closest_point(one, two)

    return closest_point(three, four)


x1, y1, x2, y2, x3, y3, x4, y4 = int(input()),\
    int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

one = (x1, y1)
two = (x2, y2)
three = (x3, y3)
four = (x4, y4)

print(longest_line(one, two, three, four))