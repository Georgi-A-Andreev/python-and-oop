def accommodate_new_pets(*args):
    result = []
    accommodated_pets = {}
    available_capacity = int(args[0])
    maximum_weight_limit = float(args[1])
    pets = args[2:]

    for pet in pets:
        if available_capacity == 0:
            result.append("You did not manage to accommodate all pets!")
            break

        if pet[1] > maximum_weight_limit:
            continue

        available_capacity -= 1
        if pet[0] not in accommodated_pets:
            accommodated_pets[pet[0]] = 0
        accommodated_pets[pet[0]] += 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    result.append('Accommodated pets:')
    for pet, count in sorted(accommodated_pets.items()):
        result.append(f'{pet}: {count}')

    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
