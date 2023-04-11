def forecast(*args):
    weather = {}
    for el in args:
        if el[0] not in args:
            weather[el[0]] = el[1]

    sorted_weather = dict(sorted(weather.items(), key=lambda x: x[0]))
    resul = ''
    for k, v in sorted_weather.items():
        if v == 'Sunny':
            resul += f'{k} - {v}\n'

    for k,v in sorted_weather.items():
        if v == 'Cloudy':
            resul += f'{k} - {v}\n'

    for k,v in sorted_weather.items():
        if v == 'Rainy':
            resul += f'{k} - {v}\n'
    return resul



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
