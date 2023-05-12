days = int(input())
plunder_per_day = int(input())
plunder_goal = float(input())

total_plunder = 0

for i in range(1, days + 1):
    total_plunder += plunder_per_day

    if i % 3 == 0:
        total_plunder += plunder_per_day / 2

    if i % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= plunder_goal:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {total_plunder / plunder_goal * 100:.2f}% of the plunder.')
