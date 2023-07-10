lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

total_expenses = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        total_expenses += helmet
    if i % 3 == 0:
        total_expenses += sword
    if i % 6 == 0:
        total_expenses += shield
    if i % 12 == 0:
        total_expenses += armor

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
