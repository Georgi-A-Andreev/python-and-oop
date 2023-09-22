rows, cols = [int(x) for x in input().split()]

start = 96

for r in range(rows):
    start += 1
    for c in range(cols):
        print(chr(start) + chr(start + c) + chr(start), end=' ')
    print()
