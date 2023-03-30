from collections import deque
from functools import reduce

text = input().split()

functions = {
    '*': lambda x: reduce(lambda a, b: int(a) * int(b), text[:x]),
    '+': lambda x: reduce(lambda a, b: int(a) + int(b), text[:x]),
    '-': lambda x: reduce(lambda a, b: int(a) - int(b), text[:x]),
    '/': lambda x: reduce(lambda a, b: int(a) // int(b), text[:x]),
}
counter = -1
while True:
    for i in text:
        counter += 1
        if str(i) in '*+-/':
            value = functions[i](counter)
            text[counter] = value
            text = text[counter:]
            counter = -1
            break
    if len(text) == 1:
        break

print(*text)
