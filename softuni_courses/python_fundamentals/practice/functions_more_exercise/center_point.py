def closest_point(one, two):
    if max([abs(i) for i in one]) <= max([abs(i) for i in two]):
        return int(one[0]), int(one[1])

    return int(two[0]), int(two[1])


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point_1 = (x1, y1)
point_2 = (x2, y2)

print(closest_point(point_1, point_2))