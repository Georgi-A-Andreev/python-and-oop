
string = list(input())
[print(string.pop(), end='') for x in range(len(string))]
