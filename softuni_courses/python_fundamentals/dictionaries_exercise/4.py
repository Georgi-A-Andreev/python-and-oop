result = {}
while True:
    x = input()

    if "-" not in x:
        break

    name, number = x.split("-")
    result[name] = number

for i in range(int(x)):
    search = input()
    if search not in result:
        print(f"Contact {search} does not exist.")
    else:
        print(f"{search} -> {result[search]}")
