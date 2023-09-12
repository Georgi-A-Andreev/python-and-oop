from collections import deque

que = deque()
while True:
    name = input()

    if name == 'End':
        print(f"{len(que)} people remaining.")
        break

    if name == 'Paid':
        while que:
            print(que.popleft())
        continue
    que.append(name)
