line = sorted([int(i) for i in input().split()], reverse=True)

line = [i for i in line if i > sum(line) / len(line)]

for i in range(min(5, len(line))):
    print(line[i], end=' ')

if not line:
    print('No')
