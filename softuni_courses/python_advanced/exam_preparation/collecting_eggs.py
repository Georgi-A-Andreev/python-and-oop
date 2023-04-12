from collections import deque

boxes = 0
eggs = deque(int(x) for x in input().split(', '))
paper = deque(int(x) for x in input().split(', '))

while eggs and paper:
    e = eggs.popleft()
    if e <= 0:
        continue
    p = paper.pop()

    if e == 13:
        paper.append(p)
        paper[0], paper[-1] = paper[-1], paper[0]

    elif e + p <= 50:
        boxes += 1

if boxes:
    print(f'Great! You filled {boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if paper:
    print(f'Pieces of paper left: {", ".join(map(str, paper))}')
