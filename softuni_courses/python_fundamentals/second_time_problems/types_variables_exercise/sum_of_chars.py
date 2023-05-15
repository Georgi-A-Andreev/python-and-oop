n = int(input())
summ = 0

for i in range(n):
    char = input()
    summ += ord(char)

print(f"The sum equals: {summ}")
