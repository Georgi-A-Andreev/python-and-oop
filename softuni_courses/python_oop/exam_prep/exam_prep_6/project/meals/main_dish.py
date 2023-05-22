from project.meals.meal import Meal


class MainDish(Meal):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity=50)

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"
