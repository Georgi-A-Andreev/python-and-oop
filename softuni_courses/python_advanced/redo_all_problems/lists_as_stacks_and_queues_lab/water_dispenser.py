from collections import deque

water = int(input())
que = deque()
while True:
    name = input()
    if name == 'Start':
        break

    que.append(name)

while True:
    command_str = input()
    if command_str == 'End':
        print(f"{water} liters left")
        break

    if command_str.isdigit():
        command = int(command_str)
        person = que.popleft()
        if command <= water:
            print(f"{person} got water")
            water -= command
        else:
            print(f"{person} must wait")
    else:
        water += int(command_str.split()[-1])
