from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = TruckDriver('A', 1)

    def test_initialization(self):
        self.assertEqual(self.truck.name, 'A')
        self.assertEqual(self.truck.money_per_mile, 1)
        self.assertEqual(self.truck.available_cargos, {})
        self.assertEqual(self.truck.earned_money, 0)
        self.assertEqual(self.truck.miles, 0)

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.truck.earned_money = -20
        self.assertEqual(str(ve.exception), "A went bankrupt.")

    def test_add_cargo_offer(self):
        self.truck.available_cargos = {'W', 2}
        with self.assertRaises(Exception) as ex:
            self.truck.add_cargo_offer('W', 2)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_normal(self):
        self.assertEqual(self.truck.add_cargo_offer('W', 2), "Cargo for 2 to W was added as an offer.")
        self.assertEqual(self.truck.available_cargos, {'W': 2})

    def test_drive_best_cargo_offer(self):
        self.assertEqual(self.truck.drive_best_cargo_offer(), "There are no offers available.")

    def test_drive_best_cargo_offer_valid(self):
        self.truck.available_cargos = {'w': 10}
        self.assertEqual(self.truck.drive_best_cargo_offer(), f"A is driving 10 to w.")
        self.assertEqual(self.truck.earned_money, 10)
        self.assertEqual(self.truck.miles, 10)

    def test_check_for_activities_inside_drive_best_cargo(self):
        self.truck.earned_money = 10000
        self.truck.available_cargos = {'a': 1000}
        self.truck.drive_best_cargo_offer()
        self.assertEqual(self.truck.earned_money, 10875)

    def test_check_for_activities(self):
        self.truck.earned_money = 10000
        self.truck.check_for_activities(1000)
        self.assertEqual(self.truck.earned_money, 9875)

    def test_eat(self):
        self.truck.earned_money = 1000
        self.truck.eat(250)
        self.assertEqual(self.truck.earned_money, 980)

    def test_sleep(self):
        self.truck.earned_money = 1000
        self.truck.sleep(1000)
        self.assertEqual(self.truck.earned_money, 955)

    def test_pump_gas(self):
        self.truck.earned_money = 1000
        self.truck.pump_gas(1500)
        self.assertEqual(self.truck.earned_money, 500)

    def test_repair_trunk(self):
        self.truck.earned_money = 10000
        self.truck.repair_truck(10000)
        self.assertEqual(self.truck.earned_money, 2500)

    def test_repr(self):
        self.truck.miles = 10
        self.assertEqual(self.truck.__repr__(), "A has 10 miles behind his back.")
