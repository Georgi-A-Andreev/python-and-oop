lines = int(input())
odd = set()
even = set()

for row in range(lines):
    name = input()
    summ = 0
    for ch in name:
        summ += ord(ch)
    div_sum = summ // (row + 1)

    if div_sum % 2 == 0:
        even.add(div_sum)
    else:
        odd.add(div_sum)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
elif sum(odd) < sum(even):
    print(*odd.symmetric_difference(even), sep=', ')
