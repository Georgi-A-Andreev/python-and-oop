n = input().split()
result = []
for i in n:
    numbers = ''
    for j in i:
        if j.isdigit():
            numbers += j

    x = i.replace(numbers, chr(int(numbers)))
    x = list(x)
    x[1], x[-1] = x[-1], x[1]
    x = ''.join(x)
    result.append(x)


print(' '.join(result))
