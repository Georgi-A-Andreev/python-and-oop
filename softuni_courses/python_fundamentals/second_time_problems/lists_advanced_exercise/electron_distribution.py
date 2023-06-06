electrons = int(input())
result = []
for i in range(1, electrons):
    result.append(0)

    if electrons - (2 * i ** 2) <= 0:
        result[i - 1] = electrons
        break

    result[i - 1] = (2 * i ** 2)
    electrons -= (2 * i ** 2)

print(result)
