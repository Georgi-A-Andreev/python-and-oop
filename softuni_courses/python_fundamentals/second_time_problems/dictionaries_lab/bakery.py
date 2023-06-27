line = input().split()
result = {}
for i in range(0, len(line), 2):
    result[line[i]] = int(line[i + 1])

print(result)
