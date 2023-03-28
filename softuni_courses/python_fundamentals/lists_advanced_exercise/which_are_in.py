n = input().split(", ")
n1 = input().split(", ")

new_list = []
for i in n:
    for j in n1:
        if i in j:
            new_list.append(i)
            break

print(new_list)
