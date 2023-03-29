result = set()

for i in range(int(input())):
    [result.add(j) for j in input().split()]

print(*result, sep='\n')
