import re

places = input()

pattern = r'(=|\/)([A-Z]{1}[A-Za-z]{1}[A-Za-z]+)\1'
match = re.findall(pattern, places)

destinations = []
travel_points = 0

for el in match:
    destinations.append(el[1])
    travel_points += len(el[1])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {travel_points}')