from collections import deque

names = deque(input().split())
turns = int(input())

while len(names) > 1:
    for _ in range(turns):
        names.append(names.popleft())

    print(f'Removed {names.pop()}')

print(f'Last is {names[0]}')
