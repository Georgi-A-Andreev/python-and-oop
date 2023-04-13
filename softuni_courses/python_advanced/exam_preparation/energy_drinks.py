from collections import deque

caffeine = deque(int(x) for x in input().split(', '))
drinks = deque(int(x) for x in input().split(', '))

starting_caffeine = 0   # max 300

while True:
    c = caffeine.pop()
    d = drinks.popleft()
    current_caffeine = c * d

    if current_caffeine + starting_caffeine <= 300:
        starting_caffeine += current_caffeine

    else:
        drinks.append(d)
        starting_caffeine = max(starting_caffeine - 30, 0)

    if not caffeine or not drinks:
        break

if drinks:
    print(f'Drinks left: {", ".join(str(x) for x in drinks)}')  # TODO with map()
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {starting_caffeine} mg caffeine.')
