from project2.client import Client
from project2.meals.dessert import Dessert
from project2.meals.main_dish import MainDish
from project2.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number):
        if client_phone_number in [i.phone_number for i in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if str(meal) not in ("Starter", "MainDish", "Dessert"):
                continue
            else:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [i.phone_number for i in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))

        for i in meal_names_and_quantities.keys():
            if i not in [meal.name for meal in self.menu]:
                raise Exception(f"{i} is not on the menu!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [i for i in self.menu if i.name == meal_name][0]

            if quantity > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        client = [i for i in self.clients_list if i.phone_number == client_phone_number][0]

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [i for i in self.menu if i.name == meal_name][0]

            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity
            meal.quantity -= quantity

        return f"Client {client_phone_number} successfully " \
               f"ordered {', '.join(i.name for i in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = [i for i in self.clients_list if i.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for i in client.shopping_cart:
            menu_meal = [meal for meal in self.menu if i.name == meal.name][0]

            menu_meal.quantity += i.quantity

        client.shopping_cart = []
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = [i for i in self.clients_list if i.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        old_bill = client.bill
        client.bill = 0
        client.shopping_cart = []

        return f"Receipt #{self.receipt_id} with total " \
               f"amount of {old_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
