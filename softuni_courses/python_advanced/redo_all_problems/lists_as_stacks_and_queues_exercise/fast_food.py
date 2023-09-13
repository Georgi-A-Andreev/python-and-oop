from collections import deque

total_food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    client = orders.popleft()
    if client > total_food:
        orders.appendleft(client)
        break

    total_food -= client

if orders:
    print(f'Orders left: {" ".join(str(x) for x in orders)}')
else:
    print('Orders complete')
