from collections import deque


rotation = 0
seats_matched = []
seats = input().split(', ')

first = deque(x for x in input().split(', '))
second = deque(x for x in input().split(', '))

while rotation < 10 and len(seats_matched) < 3:
    f = first.popleft()
    s = second.pop()
    rotation += 1
    summ = chr(int(f) + int(s))
    c_one = f + summ
    c_two = s + summ

    if c_one in seats:
        seats_matched.append(c_one)
        seats.remove(c_one)
    elif c_two in seats:
        seats_matched.append(c_two)
        seats.remove(c_two)
    else:
        first.append(f)
        second.appendleft(s)

print(f'Seat matches: {", ".join(seats_matched)}')
print(f'Rotations count: {rotation}')
