a = int(input())
n = int(input())

for i in range(n):
    l = input()

    y = ord(l) + a
    print(chr(y), end='')
