seq = input().split()
moves = 0

while True:
    turn = input()

    if turn == 'end':
        print(f'Sorry you lose :(')
        print(f'{" ".join(seq)}')
        break

    first, second = turn.split()
    first = int(first)
    second = int(second)
    moves += 1

    if first == second or first < 0 or first >= len(seq) or second < 0 or second >= len(seq):
        seq.insert(len(seq) // 2, f'-{moves}a')
        seq.insert(len(seq) // 2, f'-{moves}a')
        print('Invalid input! Adding additional elements to the board')
        continue

    if seq[first] == seq[second]:
        element = seq[first]
        seq.pop(max(first, second))
        seq.pop(min(first, second))
        print(f'Congrats! You have found matching elements - {element}!')
    elif seq[first] != seq[second]:
        print('Try again!')

    if len(seq) == 0:
        print(f'You have won in {moves} turns!')
        break
