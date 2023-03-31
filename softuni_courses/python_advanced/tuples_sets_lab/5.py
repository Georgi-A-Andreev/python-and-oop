reservations = set()
arrivals = set()

for i in range(int(input())):
    reservations.add(input())

while True:
    names = input()
    if names == 'END':
        break

    arrivals.add(names)

print(len(reservations.difference(arrivals)))
print(*sorted(reservations.difference(arrivals)), sep='\n')
