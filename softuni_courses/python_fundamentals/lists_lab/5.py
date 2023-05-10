n = int(input())

e, o, n1, p = [], [], [], []
for i in range(n):
    x = int(input())

    if x % 2 == 0:
        e.append(x)
    else:
        o.append(x)

    if x >= 0:
        p.append(x)
    else:
        n1.append(x)

c = input()

if c == 'even':
    print(e)
elif c == 'odd':
    print(o)
elif c == 'negative':
    print(n1)
else:
    print(p)
