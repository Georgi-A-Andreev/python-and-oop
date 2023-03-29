odd_set = set()
even_set = set()
ascii_sum = 0
for i in range(1, int(input()) + 1):
    name = input()
    for j in name:
        ascii_sum += ord(j)

    ascii_sum = ascii_sum // i
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)
    ascii_sum = 0
if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
