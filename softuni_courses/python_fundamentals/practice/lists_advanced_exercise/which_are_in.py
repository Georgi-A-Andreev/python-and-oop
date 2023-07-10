seq_one = input().split(', ')
seq_two = input().split(', ')

result = []

for i in seq_one:
    for j in seq_two:
        if i in j:
            result.append(i)
            break

print(result)
