n = int(input())

highest = 0
output = ''
for i in range(n):
    w = int(input())
    t = int(input())
    q = int(input())

    value = (w / t) ** q
    if value > highest:
        highest = value
        output = f'{w} : {t} = {int(value)} ({q})'

print(output)

