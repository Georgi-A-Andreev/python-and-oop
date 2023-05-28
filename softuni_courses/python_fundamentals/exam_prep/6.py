import re
cities = []
text = input()
total_points = 0
pattern = r'([\=\/])([A-Z][a-zA-Z]{2,})\1'

match = re.findall(pattern, text)

for i in match:
    cities.append(i[1])
    total_points += len(i[1])
print(f"Destinations: {', '.join(cities)}")
print(f"Travel Points: {total_points}")
