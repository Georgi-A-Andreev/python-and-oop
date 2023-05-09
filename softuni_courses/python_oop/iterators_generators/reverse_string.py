def reverse_text(string):

    while string:
        yield string[-1]
        string = string[:-1]


for char in reverse_text("step"):
    print(char, end='')
