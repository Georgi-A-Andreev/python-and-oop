names = input().split(', ')

maze = []

for _ in range(6):
    maze.append(input().split(' '))

resting = []
while True:
    current_player = names[0]

    r, c = [int(i) for i in input() if i.isdigit()]

    if current_player in resting:
        names[0], names[1] = names[1], names[0]
        resting.remove(current_player)
        continue

    if maze[r][c] == 'E':
        print(f'{current_player} found the Exit and wins the game!')
        break

    if maze[r][c] == 'T':
        print(f"{current_player} is out of the game! The winner is {names[1]}.")
        break

    if maze[r][c] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        resting.append(current_player)

    names[0], names[1] = names[1], names[0]
