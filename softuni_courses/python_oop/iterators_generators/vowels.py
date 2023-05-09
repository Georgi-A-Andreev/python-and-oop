class vowels:
    VOWELS = 'eyuioa'

    def __init__(self, string):
        self.string = [el for el in string if el.lower() in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.string:
            raise StopIteration

        return self.string.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
