capacity = 255
total = 0
n = int(input())

for _ in range(n):
    litres = int(input())

    if total + litres > capacity:
        print("Insufficient capacity!")
        continue

    total += litres

print(total)
