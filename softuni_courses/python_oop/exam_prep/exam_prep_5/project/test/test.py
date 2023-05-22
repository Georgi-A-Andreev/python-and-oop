from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Gosho', 20, 10)

    def test_initialization(self):
        self.assertEqual(self.player.name, 'Gosho')
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 10)
        self.assertEqual(self.player.wins, [])

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('g', 20, 10)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_name_setter_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('gg', 20, 10)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_setter(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('Gosho', 2, 10)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_tournament_name_not_in_wins(self):
        self.player.add_new_win('123')
        self.assertEqual(self.player.wins, ['123'])

    def test_add_new_win_tournament_in_wins(self):
        self.player.wins.append('123')
        self.assertEqual(self.player.add_new_win('123'), "123 has been already added to the list of wins!")

    def test_lt_we_are_better(self):
        other = TennisPlayer('Pesho', 25, 5)
        self.assertEqual(self.player.__lt__(other), 'Gosho is a better player than Pesho')

    def test_lt_we_are_worse(self):
        other = TennisPlayer('Pesho', 25, 15)
        self.assertEqual(self.player.__lt__(other), 'Pesho is a top seeded player and he/she is better than Gosho')

    def test_str_method(self):
        self.player.wins = ['1', '2']
        self.assertEqual(str(self.player), f"Tennis Player: Gosho\n"
                                           f"Age: 20\n"
                                           f"Points: 10.0\n"
                                           f"Tournaments won: 1, 2")


if __name__ == '__main__':
    unittest.main()
