n = input()
n = n.lower()

water = n.count('water')
fish = n.count('fish')
sun = n.count('sun')
sand = n.count('sand')

print(water + fish + sun + sand)