numbers = input().split(', ')
result = []
counter = -1

for i in numbers:
    counter += 1
    if int(i) % 2 == 0:
        result.append(counter)

print(result)