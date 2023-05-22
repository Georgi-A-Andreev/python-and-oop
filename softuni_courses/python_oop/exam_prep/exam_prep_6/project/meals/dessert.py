from project.meals.meal import Meal


class Dessert(Meal):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity=30)

    def details(self):
        return f"Dessert {self.name}: {self.price}lv/piece"
