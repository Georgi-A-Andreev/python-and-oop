from collections import deque
chocolates = 0

chocs = [int(x) for x in input().split(', ')]
cups = deque([int(x) for x in input().split(', ')])

while chocs and cups:
    ch = chocs.pop()
    if ch <= 0:
        continue
    cu = cups.popleft()

    if cu <= 0:
        chocs.append(ch)
        continue

    if ch == cu:
        chocolates += 1
        if chocs == 5:
            break
        continue

    cups.append(cu)
    chocs.append(ch - 5)

if chocolates == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocs:
    print(f"Chocolate: {', '.join(str(x) for x in chocs)}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join(str(x) for x in cups)}")
else:
    print("Milk: empty")

