n = [int(i) for i in input().split(', ')]
result = []

[result.append([]) for i in range(max(n) // 10 + 1)]

for num in n:
    if num % 10 == 0:
        result[num // 10 - 1].append(num)
        continue

    result[num // 10].append(num)

if not result[-1]:
    result.pop()

for i in range(len(result)):
    print(f"Group of {i + 1}0's: {result[i]}")
