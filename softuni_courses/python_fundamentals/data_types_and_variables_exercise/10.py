lost = int(input())

h = float(input())
s = float(input())
sh = float(input())
a = float(input())

hc, sc, shc, ac = 0, 0, 0, 0

for i in range(1, lost + 1):
    if i % 2 == 0:
        hc += 1
    if i % 3 == 0:
        sc += 1
    if i % 6 == 0:
        shc += 1
    if i % 12 == 0:
        ac += 1

expenses = hc * h + sc * s + shc * sh + ac * a
print(f'Gladiator expenses: {expenses:.2f} aureus')
