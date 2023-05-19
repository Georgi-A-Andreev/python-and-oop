import inspect

from project2.booths.open_booth import OpenBooth
from project2.booths.private_booth import PrivateBooth
from project2.delicacies.delicacy import Delicacy
from project2.booths.booth import Booth
from project2.delicacies.gingerbread import Gingerbread
from project2.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price):
        if type_delicacy not in ('Gingerbread',  'Stolen'):
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for i in self.delicacies:
            if i.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy == 'Gingerbread':
            self.delicacies.append(Gingerbread(name, price))
        else:
            self.delicacies.append(Stolen(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        if type_booth not in ("Open Booth", "Private Booth"):
            raise Exception(f"{type_booth} is not a valid booth!")

        for i in self.booths:
            if i.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == 'Open Booth':
            self.booths.append(OpenBooth(booth_number, capacity))
        else:
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        for i in self.booths:
            if not i.is_reserved and i.capacity >= number_of_people:
                i.reserve(number_of_people)
                return f"Booth {i.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):

        if booth_number not in [i.booth_number for i in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy_name not in [i.name for i in self.delicacies]:
            raise Exception(F"No {delicacy_name} in the pastry shop!")

        booth = [i for i in self.booths if i.booth_number == booth_number][0]
        delicacy = [i for i in self.delicacies if i.name == delicacy_name][0]

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = [i for i in self.booths if i.booth_number == booth_number][0]

        bill = booth.price_for_reservation
        for i in booth.delicacy_orders:
            bill += i.price

        self.income += bill

        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []

        return f"Booth {booth.booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
