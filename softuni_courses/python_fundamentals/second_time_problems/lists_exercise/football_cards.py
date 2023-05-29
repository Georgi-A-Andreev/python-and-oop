players = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

game_is_terminated = False

for i in players:
    team, number = i.split('-')
    if team == 'A':
        if int(number) in team_a:
            team_a.remove(int(number))
    else:
        if int(number) in team_b:
            team_b.remove(int(number))

    if len(team_a) < 7 or len(team_b) < 7:
        game_is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_is_terminated:
    print('Game was terminated')
