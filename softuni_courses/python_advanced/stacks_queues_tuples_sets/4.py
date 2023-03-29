from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())

total_honey = 0
functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
while bees and nectar:
    bee = bees.popleft()
    nec = nectar.pop()
    if nec >= bee:
        total_honey += abs(functions[symbols.popleft()](bee, nec))
    else:
        bees.appendleft(bee)

print(f'Total honey made: {total_honey}')
if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')
if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
