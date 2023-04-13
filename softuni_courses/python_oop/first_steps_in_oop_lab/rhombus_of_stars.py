def print_rows(rhombus_size):
    return print(f"{' ' * (rhombus_size - i)}{'* ' * i}")


size = int(input())

for i in range(1, size + 1):
    print_rows(size)

for i in range(size - 1, 0, -1):
    print_rows(size)
