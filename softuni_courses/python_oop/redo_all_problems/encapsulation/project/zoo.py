from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for w in self.workers:
            total_salaries += w.salary
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_for_animals = 0
        for a in self.animals:
            total_for_animals += a.money_for_care

        if self.__budget >= total_for_animals:
            self.__budget -= total_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = []
        result.append(f"You have {len(self.animals)} animals")
        lions = [str(l) for l in self.animals if l.__class__.__name__ == "Lion"]
        result.append(f"----- {len(lions)} Lions:")
        result += lions
        tigers = [str(l) for l in self.animals if l.__class__.__name__ == "Tiger"]
        result.append(f"----- {len(tigers)} Tigers:")
        result += tigers
        cheetahs = [str(l) for l in self.animals if l.__class__.__name__ == "Cheetah"]
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result += cheetahs

        return '\n'.join(result)

    def workers_status(self):
        result = []
        result.append(f"You have {len(self.workers)} workers")
        keepers = [str(l) for l in self.workers if l.__class__.__name__ == "Keeper"]
        result.append(f"----- {len(keepers)} Keepers:")
        result += keepers
        caretaker = [str(l) for l in self.workers if l.__class__.__name__ == "Caretaker"]
        result.append(f"----- {len(caretaker)} Caretakers:")
        result += caretaker
        vet = [str(l) for l in self.workers if l.__class__.__name__ == "Vet"]
        result.append(f"----- {len(vet)} Vets:")
        result += vet

        return '\n'.join(result)



zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
