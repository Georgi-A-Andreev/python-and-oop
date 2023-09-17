from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
process = deque(input().split())
total = 0

while working_bees and nectar:
    bee = working_bees.popleft()
    nec = nectar.pop()

    if nec >= bee:
        symbol = process.popleft()
        if symbol == '/':
            if nec == 0:
                continue
            else:
                total += abs(bee / nec)
        elif symbol == '+':
            total += abs(nec + bee)
        elif symbol == '*':
            total += abs(nec * bee)
        elif symbol == '-':
            total += abs(bee - nec)

    else:
        working_bees.appendleft(bee)
        continue

print(f"Total honey made: {total}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
