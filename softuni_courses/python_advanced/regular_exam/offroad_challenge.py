from collections import deque

fuel = deque(int(x) for x in input().split())
additional_index = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())
counter = 0
reached_top = True
result = []

while True:
    if not fuel or not additional_index:
        break
    f = fuel.pop()
    i = additional_index.popleft()
    fn = fuel_needed.popleft()
    current = f - i
    counter += 1
    if current >= fn:
        print(f"John has reached: Altitude {counter}")
        result.append(f'Altitude {counter}')
        continue

    else:
        print(f"John did not reach: Altitude {counter}")
        reached_top = False
        break

if not reached_top and result:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(result)}")
elif not reached_top and not result:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif reached_top:
    print("John has reached all the altitudes and managed to reach the top!")