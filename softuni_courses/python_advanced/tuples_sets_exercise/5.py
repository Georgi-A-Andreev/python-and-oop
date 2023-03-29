longest = []
for i in range(int(input())):
    first, second = input().split('-')

    a, b = first.split(',')
    c, d = second.split(',')

    if len(set(range(int(a), int(b) + 1)).intersection(set(range(int(c), int(d) + 1)))) > len(longest):
        longest = list(set(range(int(a), int(b) + 1)).intersection(set(range(int(c), int(d) + 1))))

print(f'Longest intersection is {longest} with length {len(longest)}')
