def team_lineup(*args):
    result = {}
    result_to_return = ''

    for v, k in args:
        if k not in result:
            result[k] = []
        result[k].append(v)

    for k, v in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        result_to_return += f'{k}:\n'
        for el in v:
            result_to_return += f'  -{el}\n'

    return result_to_return


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


