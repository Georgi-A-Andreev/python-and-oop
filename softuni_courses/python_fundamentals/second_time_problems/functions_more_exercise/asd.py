import math

def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

def print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate the distances of both lines from the origin
    distance_line1 = distance_from_origin(x1, y1) + distance_from_origin(x2, y2)
    distance_line2 = distance_from_origin(x3, y3) + distance_from_origin(x4, y4)

    # Compare the distances and print the longer line
    if distance_line1 >= distance_line2:
        print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
    else:
        print(f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")

x1, y1, x2, y2, x3, y3, x4, y4 = int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input())

print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)