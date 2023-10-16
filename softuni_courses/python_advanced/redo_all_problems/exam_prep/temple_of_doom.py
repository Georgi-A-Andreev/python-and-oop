from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = deque([int(x) for x in input().split()])

while True:
    t = tools.popleft()
    s = substances.pop()

    current = t * s

    if current in challenges:
        challenges.remove(current)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break
        if not tools or not substances:
            print("Harry is lost in the temple. Oblivion awaits him.")
            break
        continue

    tools.append(t + 1)
    if s != 1:
        substances.append(s - 1)

    if not tools or not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break


if tools:
    print(f'Tools: {", ".join(str(x) for x in tools)}')

if substances:
    print(f'Substances: {", ".join(str(x) for x in substances)}')

if challenges:
    print(f'Challenges: {", ".join(str(x) for x in challenges)}')
