line = input().split()
products = {}

for num in range(0, len(line), 2):
    products[line[num]] = int(line[num + 1])

for el in input().split():
    if el in products:
        print(f"We have {products[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")
