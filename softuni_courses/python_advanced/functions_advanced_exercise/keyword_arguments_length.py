def kwargs_length(**data):
    return len(data)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
