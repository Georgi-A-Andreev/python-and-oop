n = input().split()
x = int(input())
n1 = []
for i in n:
    n1.append(int(i))

for _ in range(x):
    y = float("inf")
    for j in range(len(n1)):
        if n1[j] < y:
            y = n1[j]
    n1.remove(y)

for i1 in range(len(n1)):
    if i1 == len(n1) - 1:
        print(n1[i1])
    else:
        print(n1[i1], end=", ")


