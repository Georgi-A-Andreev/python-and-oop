clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack = rack_capacity
total_racks = 1
while clothes:
    current = clothes.pop()

    if current > current_rack:
        total_racks += 1
        current_rack = rack_capacity
        clothes.append(current)

    else:
        current_rack -= current

print(total_racks)