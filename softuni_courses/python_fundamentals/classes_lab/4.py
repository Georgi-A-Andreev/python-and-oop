class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        string = ''
        if species == 'mammal':
            string = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal" \
               f" animals: {Zoo.__animals}"
        elif species == 'fish':
            string = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal" \
               f" animals: {Zoo.__animals}"
        if species == 'bird':
            string = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal" \
               f" animals: {Zoo.__animals}"
        return string


zoo = Zoo(input())
count = int(input())

for _ in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

print(zoo.get_info(input()))
