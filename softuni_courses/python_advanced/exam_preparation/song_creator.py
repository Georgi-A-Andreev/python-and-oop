def add_songs(*args):
    result = {}
    final_result = ''
    for title, lyrics in args:
        if title not in result:
            result[title] = ''
        for row in lyrics:
            result[title] += f'{row}\n'

    for k, v in result.items():
        final_result += f'- {k}\n{v}'

    return final_result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

