from project2.meals.meal import Meal


class MainDish(Meal):
    def __init__(self, name, price, quantity=50):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"

    def __str__(self):
        return 'MainDish'