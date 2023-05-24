n = int(input())

total_sum = 0

for i in range(n):
    a = input()
    total_sum += ord(a)

print(f'The sum equals: {total_sum}')
