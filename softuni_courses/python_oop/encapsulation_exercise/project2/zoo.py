class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for i in self.workers:
            if i.name == worker_name:
                self.workers.remove(i)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for i in self.workers:
            salaries += i.salary

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        care_money = 0
        for i in self.animals:
            care_money += i.money_for_care

        if care_money <= self.__budget:
            self.__budget -= care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = 0
        tigers = 0
        cheetahs = 0
        for i in self.animals:
            if i.__class__.__name__ == "Lion":
                lions += 1
            elif i.__class__.__name__ == "Tiger":
                tigers += 1
            elif i.__class__.__name__ == 'Cheetah':
                cheetahs += 1
        result = ""
        result += f"You have {len(self.animals)} animals\n"
        result += f'----- {lions} Lions:\n'
        result += '\n'.join([str(i) for i in self.animals if i.__class__.__name__ == 'Lion'])
        result += f"\n----- {tigers} Tigers:\n"
        result += '\n'.join([str(i) for i in self.animals if i.__class__.__name__ == 'Tiger'])
        result += f"\n----- {cheetahs} Cheetahs:\n"
        result += '\n'.join([str(i) for i in self.animals if i.__class__.__name__ == 'Cheetah'])

        return result

    def workers_status(self):
        keepers = 0
        caretakers = 0
        vets = 0
        for i in self.workers:
            if i.__class__.__name__ == 'Keeper':
                keepers += 1
            elif i.__class__.__name__ == 'Caretaker':
                caretakers += 1
            elif i.__class__.__name__ == 'Vet':
                vets += 1
        result = ''
        result += f"You have {len(self.workers)} workers\n"
        result += f"----- {keepers} Keepers:\n"
        result += '\n'.join(str(i) for i in self.workers if i.__class__.__name__ == 'Keeper')
        result += f"\n----- {caretakers} Caretakers:\n"
        result += '\n'.join(str(i) for i in self.workers if i.__class__.__name__ == 'Caretaker')
        result += f"\n----- {vets} Vets:\n"
        result += '\n'.join(str(i) for i in self.workers if i.__class__.__name__ == 'Vet')

        return result
