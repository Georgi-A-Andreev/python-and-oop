line = input().split()
my_dict = {}

for i in range(0, len(line), 2):
    product = line[i]
    quantity = int(line[i + 1])
    my_dict[product] = quantity

search = input().split()
for search in search:
    if search in my_dict:
        print(f'We have {my_dict[search]} of {search} left')
    else:
        print(f"Sorry, we don't have {search}")
        