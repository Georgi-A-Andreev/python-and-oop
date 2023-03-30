from collections import deque

chocolate = deque(input().split(', '))
cups_of_milk = deque(input().split(', '))

milkshakes = 0

while milkshakes != 5:
    if len(chocolate) == 0 or len(cups_of_milk) == 0:
        break
    valid = True
    x = chocolate.pop()
    y = cups_of_milk.popleft()
    if int(x) <= 0:
        cups_of_milk.appendleft(y)
        valid = False
    elif int(y) <= 0:
        chocolate.append(x)
        valid = False
    if not valid:
        continue
    if int(x) == int(y):
        milkshakes += 1
    else:
        cups_of_milk.append(y)
        chocolate.append(str(int(x) - 5))

print('Great! You made all the chocolate milkshakes needed!')\
    if milkshakes == 5 else print('Not enough milkshakes.')
print(f'Chocolate: {", ".join(chocolate)}') \
    if len(chocolate) > 0 else print('Chocolate: empty')
print(f'Milk: {", ".join(cups_of_milk)}') \
    if len(cups_of_milk) > 0 else print('Milk: empty')
