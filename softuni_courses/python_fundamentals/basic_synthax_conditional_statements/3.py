n = input().split(", ")

if n[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(n) - (n.index('wolf') + 1)}! You are about to be eaten by a wolf!")
