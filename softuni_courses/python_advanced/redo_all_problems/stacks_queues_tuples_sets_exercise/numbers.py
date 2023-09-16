first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'Add' and command[1] == 'First':
        for el in range(2, len(command)):
            first_seq.add(int(command[el]))

    elif command[0] == 'Add' and command[1] == 'Second':
        for el in range(2, len(command)):
            second_seq.add(int(command[el]))

    elif command[0] == 'Remove' and command[1] == 'First':
        for el in range(2, len(command)):
            if int(command[el]) in first_seq:
                first_seq.remove(int(command[el]))

    elif command[0] == 'Remove' and command[1] == 'Second':
        for el in range(2, len(command)):
            if int(command[el]) in second_seq:
                second_seq.remove(int(command[el]))

    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print(True)
        else:
            print(False)

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')
