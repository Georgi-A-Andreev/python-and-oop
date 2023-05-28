waiting_people = int(input())
starting_state = [int(x) for x in input().split()]
counter = -1

for i in starting_state:
    counter += 1
    while starting_state[counter] < 4:
        if waiting_people <= 0:
            print('The lift has empty spots!')
            [print(j, end=" ") for j in starting_state]
            exit()
        waiting_people -= 1
        starting_state[counter] += 1

if starting_state[counter] == 4 and waiting_people == 0:
    [print(j, end=" ") for j in starting_state]
    exit()
print(f"There isn't enough space! {waiting_people} people in a queue!")
[print(j, end=" ") for j in starting_state]
