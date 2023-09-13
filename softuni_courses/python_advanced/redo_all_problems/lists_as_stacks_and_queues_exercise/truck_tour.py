from collections import deque

total_stops = int(input())
stops_info = deque()
for _ in range(total_stops):
    stops_info.append([int(x) for x in input().split()])  # gas / distance

counter = 0
found = False
while True:
    current_gas = 0
    for gas, distance in stops_info:
        current_gas += gas
        if current_gas < distance:
            break
        else:
            current_gas -= distance
    else:
        found = True

    if found:
        print(counter)
        break
    else:
        counter += 1
        stops_info.append(stops_info.popleft())
