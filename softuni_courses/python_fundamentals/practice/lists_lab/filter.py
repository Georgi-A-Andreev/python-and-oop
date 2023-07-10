lst = []

for i in range(int(input())):
    lst.append(int(input()))

command = input()
result = None

if command == 'even':
    result = [i for i in lst if i % 2 == 0]

elif command == 'odd':
    result = [i for i in lst if i % 2 != 0]

elif command == 'positive':
    result = [i for i in lst if i >= 0]

elif command == 'negative':
    result = [i for i in lst if i < 0]

print(result)
