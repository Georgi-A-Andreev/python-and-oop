pieces = int(input())
my_dict = {}
for i in range(pieces):
    piece, composer, key = input().split('|')
    if piece not in my_dict:
        my_dict[piece] = [composer, key]


while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split("|")

    if command[0] == 'Add':
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in my_dict:
            print(f"{piece} is already in the collection!")
        else:
            my_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == 'Remove':
        piece = command[1]
        if piece not in my_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            my_dict.pop(piece)
            print(f"Successfully removed {piece}!")
    else:
        piece = command[1]
        new_key = command[2]
        if piece in my_dict:
            my_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


for piece, my_list in my_dict.items():
    print(f"{piece} -> Composer: {my_dict[piece][0]}, Key: {my_dict[piece][1]}")
