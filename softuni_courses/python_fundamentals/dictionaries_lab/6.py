x = input().lower().split()
result = {}
for i in x:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

for x in result:
    if result[x] % 2 != 0:
        print(x, end=' ')
