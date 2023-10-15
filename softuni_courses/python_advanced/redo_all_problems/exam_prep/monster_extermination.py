from collections import deque

armor = deque([int(x) for x in input().split(',')])
striking = deque([int(x) for x in input().split(',')])
monsters_killed = 0

while True:
    monster = armor.popleft()
    damage = striking.pop()

    if damage >= monster:
        monsters_killed += 1
        if striking:
            striking[-1] += damage - monster
        else:
            if damage - monster:
                striking.append(damage - monster)
    else:
        armor.append(monster - damage)

    if not armor or not striking:
        break

if not armor:
    print("All monsters have been killed!")
if not striking:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
