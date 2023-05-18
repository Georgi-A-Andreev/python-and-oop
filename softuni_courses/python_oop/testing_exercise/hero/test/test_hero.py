import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('imba', 10, 100, 100)
        self.enemy = Hero('imba2', 5, 50, 50)

    def test_constructor(self):
        self.assertEqual(self.hero.username, 'imba')
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_same_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), 'You cannot fight yourself')

    def test_battle_low_hero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_health_too_low(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ve.exception), "You cannot fight imba2. He needs to rest")

    def test_battle_draw(self):
        self.assertEqual(self.hero.battle(self.enemy), 'Draw')

    def test_enemy_hero_low_hp(self):
        self.enemy.level = 0

        self.assertEqual(self.hero.battle(self.enemy), 'You win')
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 105)
        self.assertEqual(self.hero.damage, 105)

    def test_battle_our_heal_too_low(self):
        self.hero.level = 0
        self.assertEqual(self.hero.battle(self.enemy), 'You lose')
        self.assertEqual(self.enemy.level, 6)
        self.assertEqual(self.enemy.health, 55)
        self.assertEqual(self.enemy.damage, 55)

    def test_str_method(self):
        self.assertEqual(str(self.hero), f"Hero imba: 10 lvl\n"
               f"Health: 100\n"
               f"Damage: 100\n")


if __name__ == '__main__':
    unittest.main()
