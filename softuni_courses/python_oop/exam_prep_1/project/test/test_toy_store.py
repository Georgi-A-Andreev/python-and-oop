from project2.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_constructor(self):
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('Z', 'abv')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_same_toy(self):
        self.toy.toy_shelf['A'] = 'M'
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'M')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_taken_shelf(self):
        self.toy.toy_shelf['A'] = 'M'
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'N')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_correct_add_toy(self):
        self.assertEqual(self.toy.add_toy('A', 'B'), "Toy:B placed successfully!")
        self.assertEqual(self.toy.toy_shelf, {
            "A": 'B',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_toy_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('M', 'G')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_wrong_toy(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('A', 'A')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

        self.toy.add_toy('A', 'B')
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('A', 'A')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_correct(self):
        self.toy.toy_shelf['A'] = 'A'
        self.assertEqual(self.toy.remove_toy('A', 'A'), "Remove toy:A successfully!")
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })


if __name__ == '__main__':
    unittest.main()
