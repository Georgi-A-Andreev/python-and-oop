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
        if species == 'bird':
            names = ', '.join(self.birds)
            res = 'Birds'
        elif species == 'mammal':
            names = ', '.join(self.mammals)
            res = 'Mammals'
        else:
            names = ', '.join(self.fishes)
            res = 'Fishes'
        return f"{res} in {self.name}: {names}\nTotal animals: {self.__animals}"


zoo = Zoo(input())
n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

print(zoo.get_info(input()))
