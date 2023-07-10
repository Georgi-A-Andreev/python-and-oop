lst = input().split(', ')

if lst[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:

    print(f"Oi! Sheep number {len(lst) - lst.index('wolf') -1}! You are about to be eaten by a wolf!")
