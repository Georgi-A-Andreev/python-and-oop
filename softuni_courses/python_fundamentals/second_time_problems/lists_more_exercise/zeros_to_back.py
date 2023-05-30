my_list = [int(i) for i in input().split(', ')]
counter = 0

for el in my_list:
    if el == 0:
        counter += 1

for i in range(counter):
    my_list.remove(0)
    my_list.append(0)

print(my_list)
