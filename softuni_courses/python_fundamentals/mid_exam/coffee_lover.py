coffee_stock = input().split()
n = int(input())

for _ in range(n):
    line = input().split()

    command = line[0]

    if command == 'Include':
        coffee_stock.append(line[1])

    elif command == 'Remove':
        if int(line[-1]) > len(coffee_stock):
            continue

        if line[1] == 'first':
            for _ in range(int(line[-1])):
                coffee_stock.pop(0)

        elif line[1] == 'last':
            for _ in range(int(line[-1])):
                coffee_stock.pop()

    elif command == 'Prefer':
        idx1 = int(line[1])
        idx2 = int(line[2])

        if idx1 < 0 or idx1 >= len(coffee_stock) or idx2 < 0 or idx2 >= len(coffee_stock):
            continue

        coffee_stock[idx1], coffee_stock[idx2] = coffee_stock[idx2], coffee_stock[idx1]

    elif command == 'Reverse':
        coffee_stock = reversed(coffee_stock)

print('Coffees:')
print(" ".join(coffee_stock))
