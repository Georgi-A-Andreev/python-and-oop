numbers = [int(i) for i in input().split()]
count = int(input())


for i in range(count):
    min_number = float('inf')

    for j in numbers:
        if j < min_number:
            min_number = j

    numbers.remove(min_number)

print(', '.join(str(x) for x in numbers))
