n = input().split()
first = []
second = []
do_break = False

for i in n:
    n1 = i.split("-")
    team = n1[0]
    player = n1[1]

    if team == "A":
        if n1 not in first:
            first.append(n1)
    else:
        if n1 not in second:
            second.append(n1)
    if len(first) > 4 or len(second) > 4:
        do_break = True
        break

print(f"Team A - {11 - len(first)}; Team B - {11 - len(second)}")
if do_break:
    print("Game was terminated")
