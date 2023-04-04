total_presents = int(input())
rows = int(input())
hood = []
my_pos = []
nice_kids = 0
bad_kids = 0
good_kids = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(rows):
    hood.append(input().split())
    if 'S' in hood[r]:
        my_pos = [r, hood[r].index('S')]
    if 'V' in hood[r]:
        nice_kids += hood[r].count('V')

while total_presents:
    command = input()

    if command == 'Christmas morning':
        break
    hood[my_pos[0]][my_pos[1]] = '-'

    my_pos[0] += directions[command][0]
    my_pos[1] += directions[command][1]

    if 0 <= my_pos[0] < rows and 0 <= my_pos[1] < rows:
        if hood[my_pos[0]][my_pos[1]] == 'V':
            total_presents -= 1
            good_kids += 1

        elif hood[my_pos[0]][my_pos[1]] == 'C':
            for d in directions.values():
                if hood[my_pos[0] + d[0]][my_pos[1] + d[1]] == 'V':
                    total_presents -= 1
                    good_kids += 1
                elif hood[my_pos[0] + d[0]][my_pos[1] + d[1]] == 'X':
                    total_presents -= 1
                hood[my_pos[0] + d[0]][my_pos[1] + d[1]] = '-'
    else:
        break
    hood[my_pos[0]][my_pos[1]] = 'S'

if total_presents <= 0 and nice_kids > good_kids:
    print("Santa ran out of presents!")

[print(*i) for i in hood]

if good_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - good_kids} nice kid/s.")
