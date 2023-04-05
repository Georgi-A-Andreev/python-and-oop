from collections import deque


def create_field(row, col):
    field = []
    for _ in range(row):
        field.append([0] * col)
    return field


max_players = deque(range(1, int(input('How many players will play? : ')) + 1))
rows = int(input('How many rows? : '))
cols = int(input('How many cols? : '))
matrix = create_field(rows, cols)

we_got_a_winner = False

while True:
    try:
        while True:
            current_player = max_players[0]
            choice = int(input(f'Player {current_player}, please choose a column:\n')) - 1

            for i in range(len(matrix) - 1, -1, -1):
                if matrix[i][choice] == 0:
                    matrix[i][choice] = current_player
                    [print(i) for i in matrix]
                    break

            for i in range(len(matrix)):   # validate horizontal
                for j in matrix[i]:
                    if j == 1 or j == 2:
                        lst = matrix[i][matrix[i].index(j):min(matrix[i].index(j) + 4, len(matrix[i]))]
                        if len(lst) == 4 and len(set(lst)) == 1:
                            we_got_a_winner = True

            for i in range(len(matrix)):   # validate vertical
                for j in matrix[i]:
                    if j == 1 or j == 2:
                        if matrix[i].index(j) <= len(matrix[i]) - 4:
                            lst = [matrix[i][matrix[i].index(j)], matrix[i - 1][matrix[i].index(j)],
                                   matrix[i - 2][matrix[i].index(j)], matrix[i - 3][matrix[i].index(j)]]
                            if len(lst) == 4 and len(set(lst)) == 1:
                                we_got_a_winner = True

            for i in range(len(matrix)):   # validate diagonal going up right
                for j in matrix[i]:
                    if j == 1 or j == 2:
                        if i >= 3 and matrix[i].index(j) <= len(matrix[i]) - 4:
                            lst = [matrix[i][matrix[i].index(j)], matrix[i - 1][matrix[i].index(j) + 1],
                                   matrix[i - 2][matrix[i].index(j) + 2], matrix[i - 3][matrix[i].index(j) + 3]]
                            if len(lst) == 4 and len(set(lst)) == 1:
                                we_got_a_winner = True

            for i in range(len(matrix)):   # validate diagonal going up left
                for j in matrix[i]:
                    if j == 1 or j == 2:
                        if i >= 3 and matrix[i].index(j) >= 3:
                            lst = [matrix[i][matrix[i].index(j)], matrix[i - 1][matrix[i].index(j) - 1],
                                   matrix[i - 2][matrix[i].index(j) - 2], matrix[i - 3][matrix[i].index(j) - 3]]
                            if len(lst) == 4 and len(set(lst)) == 1:
                                we_got_a_winner = True

            if we_got_a_winner:
                print(f'The winner is player {current_player}')
                exit()
            max_players.append(max_players.popleft())

    except IndexError:
        print("Please enter valid position")
