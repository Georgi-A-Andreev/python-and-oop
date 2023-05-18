import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('some_name', 'some type', 'some sound')

    def test_correct_initialization(self):
        self.assertTrue(self.mammal.name, 'some name')
        self.assertTrue(self.mammal.type, 'some type')
        self.assertTrue(self.mammal.sound, 'some sound')

    def test_get_kingdom(self):
        self.assertTrue(self.mammal.get_kingdom(), 'animals')

    def test_make_sound(self):
        self.assertTrue(self.mammal.make_sound(), "some name makes some sound")

    def test_get_info(self):
        self.assertTrue(self.mammal.info(), "some name is of type some type")


if __name__ == '__main__':
    unittest.main()
