def words_sorting(*args):
    result = {}
    text = ''

    for i in args:
        if i not in result:
            result[i] = 0

    for k in result:
        for j in k:
            result[k] += ord(j)

    sum_values = sum(v for v in result.values())

    if sum_values % 2 == 0:
        for k in sorted(result.items(), key=lambda x: x[0]):
            text += f'{k[0]} - {k[1]}\n'
    else:
        for k in sorted(result.items(), key=lambda x: -x[1]):
            text += f'{k[0]} - {k[1]}\n'

    return text


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
