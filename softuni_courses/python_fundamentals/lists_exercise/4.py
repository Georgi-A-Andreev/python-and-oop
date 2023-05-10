n = input().split(", ")
c = int(input())

new = [0] * c

for i in range(len(n)):
    new[i % c] += int(n[i])

print(new)
