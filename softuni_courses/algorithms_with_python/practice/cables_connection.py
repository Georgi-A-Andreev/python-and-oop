first = [int(x) for x in input().split()]

lis = [1] * len(first)

for idx in range(len(first)):
    for idx2 in range(idx - 1, -1, -1):
        if first[idx] > first[idx2]:
            lis[idx] = max(lis[idx2] + 1, lis[idx])

print(f'Maximum pairs connected: {max(lis)}')
