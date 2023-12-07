import unittest
from testing_first_exam.trip import Trip


class TestTrip(unittest.TestCase):
    def setUp(self):
        self.first = Trip(10000, 1, False)
        self.second = Trip(10000, 1, True)
        self.third = Trip(10000, 1, False)

    def test_constructor(self):
        self.assertEqual(self.first.budget, 10000)
        self.assertEqual(self.first.travelers, 1)
        self.assertFalse(self.first.is_family)
        self.assertFalse(self.first.booked_destinations_paid_amounts)

    def test_setters(self):
        with self.assertRaises(ValueError) as ve:
            self.first.travelers = 0
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

        self.assertFalse(self.second.is_family)

    def test_book_a_trip(self):
        self.assertEqual(self.first.book_a_trip('asdasd'),
                         'This destination is not in our offers, please choose a new one!')
        self.first.budget = 100
        self.assertEqual(self.first.book_a_trip('New Zealand'), 'Your budget is not enough!')
        self.assertEqual(self.third.book_a_trip('New Zealand'),
                         'Successfully booked destination New Zealand! Your budget left is 2500.00')
        self.assertEqual(self.third.budget, 2500)
        self.assertEqual(len(self.third.booked_destinations_paid_amounts), 1)

    def test_booking_status(self):
        self.assertEqual(self.first.booking_status(), 'No bookings yet. Budget: 10000.00')
        self.first.book_a_trip('New Zealand')
        self.assertEqual(self.first.booking_status(), """Booked Destination: New Zealand
Paid Amount: 7500.00\nNumber of Travelers: 1\nBudget Left: 2500.00""")


if __name__ == '__main__':
    unittest.main()