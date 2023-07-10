n = int(input())

for i in range(1, n + 1):
    result = 0
    flag = None
    for el in str(i):
        result += int(el)

    if result in (5, 7, 11):
        flag = True
    else:
        flag = False

    print(f'{i} -> {flag}')
