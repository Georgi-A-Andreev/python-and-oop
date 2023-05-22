import unittest
from project2.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 1000)

    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.capacity, 100)
        self.assertEqual(self.vehicle.horse_power, 1000)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual(str(ex.exception), 'Not enough fuel')

        self.vehicle.drive(1)
        self.assertEqual(self.vehicle.fuel, 98.75)

    def test_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)
        self.assertEqual(str(ex.exception), 'Too much fuel')

        self.vehicle.fuel = 10
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 20)

    def test_str_method(self):
        self.assertEqual(str(self.vehicle), f"The vehicle has 1000 "
                                               f"horse power with 100 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()