result = {}

while True:
    line = input()

    if ":" not in line:
        break

    name, idd, course = line.split(":")

    if course not in result:
        result[course] = [name, idd]
    else:
        result[course].append(name)
        result[course].append(idd)

line = " ".join(line.split("_"))
for i in range(0, len(result[line]), 2):
    print(f"{result[line][i]} - {result[line][i + 1]}")
