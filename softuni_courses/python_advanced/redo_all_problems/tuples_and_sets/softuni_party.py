guests = int(input())
arrivals = []
for _ in range(guests):
    arrivals.append(input())

while True:
    guest = input()
    if guest == 'END':
        break

    arrivals.remove(guest)

print(len(arrivals))
print(*sorted(arrivals), sep='\n')
