
countries = input().split(", ")
cities = input().split(", ")

result = dict(zip(countries, cities))
for i, y in result.items():
    print(f"{i} -> {y}")
