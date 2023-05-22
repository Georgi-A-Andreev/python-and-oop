from project2.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('m', 'mt', 'ms')

    def test_initialization(self):
        self.assertEqual(self.mammal.name, 'm')
        self.assertEqual(self.mammal.type, 'mt')
        self.assertEqual(self.mammal.sound, 'ms')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "m makes ms")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info(self):
        self.assertEqual(self.mammal.info(), "m is of type mt")


if __name__ == '__main__':
    unittest.main()