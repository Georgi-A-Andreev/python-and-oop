from collections import deque

bows_of_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bows_of_ramen and customers:
    ramen = bows_of_ramen.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue

    elif ramen > customer:
        bows_of_ramen.append(ramen - customer)

    else:
        customers.appendleft(customer - ramen)

if not customers:
    print('Great job! You served all the customers.')
    if bows_of_ramen:
        print(f'Bowls of ramen left: {", ".join(str(x) for x in bows_of_ramen)}')
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
