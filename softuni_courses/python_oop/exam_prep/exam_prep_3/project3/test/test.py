from project3.robot import Robot
import unittest


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot('1', 'Education', 50, 100)

    def test_allowed_categories(self):
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)

    def test_initialization(self):
        self.assertEqual(self.robot.robot_id, '1')
        self.assertEqual(self.robot.category, 'Education')
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_category_setter(self):
        with self.assertRaises(ValueError) as ve:
            Robot('1', '2', 50, 50)
        self.assertEqual(str(ve.exception),
                         f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ve:
            Robot('1', 'Education', 50, -10)
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_proper_setter(self):
        other = Robot('1', 'Entertainment', 10, 20)
        self.assertEqual(other.category, 'Entertainment')

    def test_upgrade_component_already_in(self):
        self.robot.hardware_upgrades.append('123')
        self.assertEqual(self.robot.upgrade('123', 123), "Robot 1 was not upgraded.")

    def test_upgrade_proper(self):
        self.assertEqual(self.robot.upgrade('123', 100), 'Robot 1 was upgraded with 123.')
        self.assertEqual(self.robot.hardware_upgrades, ['123'])
        self.assertEqual(self.robot.price, 250)

    def test_update_software_updates_and_version_lower(self):
        self.robot.software_updates = [10]
        self.assertEqual(self.robot.update(5, 5), "Robot 1 was not updated.")

    def test_update_capacity(self):
        self.assertEqual(self.robot.update(5, 55), "Robot 1 was not updated.")

    def test_proper_update_function(self):
        self.assertEqual(self.robot.update(5, 5), 'Robot 1 was updated to version 5.')
        self.assertEqual(self.robot.software_updates, [5])
        self.assertEqual(self.robot.available_capacity, 45)

    def test_gt_high_price(self):
        other = Robot('2', 'Military', 40, 80)
        self.assertEqual(self.robot.__gt__(other), 'Robot with ID 1 is more expensive than Robot with ID 2.')

    def test_gt_equal(self):
        other = Robot('2', 'Military', 50, 100)
        self.assertEqual(self.robot.__gt__(other), 'Robot with ID 1 costs equal to Robot with ID 2.')

    def test_gt_smaller(self):
        other = Robot('2', 'Military', 60, 200)
        self.assertEqual(self.robot.__gt__(other), 'Robot with ID 1 is cheaper than Robot with ID 2.')


if __name__ == '__main__':
    unittest.main()
