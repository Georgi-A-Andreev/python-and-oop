from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart('Qwert', 100)

    def test_initialization(self):
        self.assertEqual(self.cart.shop_name, 'Qwert')
        self.assertEqual(self.cart.budget, 100)
        self.assertEqual(self.cart.products, {})

    def test_shop_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('qwert', 100)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_name_setter_isalpha(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('Q1we', 100)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_too_high_product_price(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('qwerty', 120)
        self.assertEqual(str(ve.exception), "Product qwerty cost too much!")

    def test_add_to_cart_equal_product_price(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('qwerty', 100)
        self.assertEqual(str(ve.exception), "Product qwerty cost too much!")

    def test_add_to_card_correct(self):
        self.assertEqual(self.cart.add_to_cart('123', 50), "123 product was successfully added to the cart!")
        self.assertEqual(self.cart.products, {'123': 50})

    def test_remove_from_cart_product_in(self):
        self.cart.products = {'123': 40}
        self.assertEqual(self.cart.remove_from_cart('123'), "Product 123 was successfully removed from the cart!")
        self.assertEqual(self.cart.products, {})

    def test_remove_from_cart_product_not_in(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('123')
        self.assertEqual(str(ve.exception), "No product with name 123 in the cart!")

    def test_add_other(self):
        other = ShoppingCart('Qwe', 30)
        other.products = {'rrr', 45}
        new = self.cart.__add__(other)
        self.assertEqual(new.budget, 130)
        self.assertEqual(new.products, {'rrr': 45})
        self.assertEqual(new.shop_name, 'QwertQwe')

    def test_buy_products(self):
        self.cart.products = {'123': 55, '234': 60}
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 15.00lv!")

    def test_buy_products_correct(self):
        self.cart.products = {'123': 45, '234': 45}
        self.assertEqual(self.cart.buy_products(), 'Products were successfully bought! Total cost: 90.00lv.')


if __name__ == '__main__':
    unittest.main()