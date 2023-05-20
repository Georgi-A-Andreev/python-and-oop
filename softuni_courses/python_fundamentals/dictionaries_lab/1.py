line = input().split()
result = {}

for index, word in enumerate(line):
    if index % 2 == 0:
        result[word] = int(line[index + 1])

print(result)