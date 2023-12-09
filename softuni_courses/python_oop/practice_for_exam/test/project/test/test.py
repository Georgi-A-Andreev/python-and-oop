import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.f = RailwayStation('Gosho')

    def test_constructor(self):
        self.assertEqual(self.f.name, 'Gosho')
        self.assertEqual(self.f.arrival_trains, deque())
        self.assertEqual(self.f.departure_trains, deque())

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.f.name = 'g'
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")
        with self.assertRaises(ValueError) as ve:
            self.f.name = 'gee'
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.f.new_arrival_on_board('qwe')
        self.assertEqual(len(self.f.arrival_trains), 1)
        self.assertEqual(self.f.arrival_trains.popleft(), 'qwe')

    def test_train_has_arrived(self):
        self.f.new_arrival_on_board('1')
        self.assertEqual(self.f.train_has_arrived('2'), "There are other trains to arrive before 2.")
        self.assertEqual(self.f.train_has_arrived('1'), "1 is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.f.departure_trains[0], '1')
        self.assertEqual(len(self.f.arrival_trains), 0)

    def test_train_last_left(self):
        self.assertFalse(self.f.train_has_left('1'))
        self.f.arrival_trains.append('1')
        self.f.departure_trains.append('2')
        self.assertFalse(self.f.train_has_left('3'))
        self.assertTrue(self.f.train_has_left('2'))
        self.assertEqual(len(self.f.departure_trains), 0)




if __name__ == '__main__':
    unittest.main()