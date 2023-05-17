n = int(input())
my_dict = {}

for _ in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality
    my_dict[value] = [weight, time_needed, quality]

x = max(my_dict.keys())
print(f"{my_dict[x][0]} : {my_dict[x][1]} = {max(my_dict.keys()):.0f} ({my_dict[x][2]})")
