from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity=60)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
