result = {}

for i in range(int(input())):
    name, grade = input().split()

    if name not in result:
        result[name] = []

    result[name].append(float(grade))

for n, g in result.items():
    print(f"{n} -> {' '.join([f'{x:.2f}' for x in result[n]])} "
          f"(avg: {sum(result[n]) / len(result[n]):.2f})")
