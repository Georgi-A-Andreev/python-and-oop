import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from django.db.models import Count, Sum, F

from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and check models
def add_records_to_database():
    # Categories
    food_category = Category.objects.create(name='Food')
    drinks_category = (Category.objects.create(name='Drinks'))

    # Food
    product1 = Product.objects.create(name='Pizza', description='Delicious pizza with toppings', price=10.99, category=food_category, is_available=False)
    product2 = Product.objects.create(name='Burger', description='Classic burger with cheese and fries', price=7.99, category=food_category, is_available=False)
    product3 = Product.objects.create(name='Apples', description='A bag of juicy red apples', price=3.99, category=food_category, is_available=True)
    product4 = Product.objects.create(name='Bread', description='A freshly baked loaf of bread', price=2.49, category=food_category, is_available=True)
    product5 = Product.objects.create(name='Pasta and Sauce Bundle', description='Package containing pasta and a jar of pasta sauce', price=6.99, category=food_category, is_available=False)
    product6 = Product.objects.create(name='Tomatoes', description='A bundle of ripe, red tomatoes', price=2.99, category=food_category, is_available=True)
    product7 = Product.objects.create(name='Carton of Eggs', description='A carton containing a dozen fresh eggs', price=3.49, category=food_category, is_available=True)
    product8 = Product.objects.create(name='Cheddar Cheese', description='A block of aged cheddar cheese', price=7.99, category=food_category, is_available=False)
    product9 = Product.objects.create(name='Milk', description='A gallon of fresh cow milk', price=3.49, category=food_category, is_available=True)

    # Drinks
    product10 = Product.objects.create(name='Coca Cola', description='Refreshing cola drink', price=1.99, category=drinks_category, is_available=True)
    product11 = Product.objects.create(name='Orange Juice', description='Freshly squeezed orange juice', price=2.49, category=drinks_category, is_available=False)
    product12 = Product.objects.create(name='Bottled Water', description='A 12-pack of purified bottled water', price=4.99, category=drinks_category, is_available=True)
    product13 = Product.objects.create(name='Orange Soda', description='A 6-pack of carbonated orange soda', price=5.49, category=drinks_category, is_available=True)
    product14 = Product.objects.create(name='Bottled Green Tea', description='A bottled green tea', price=3.99, category=drinks_category, is_available=False)
    product15 = Product.objects.create(name='Beer', description='A bottled craft beer', price=5.49, category=drinks_category, is_available=True)

    # Customers
    customer1 = Customer.objects.create(username='john_doe')
    customer2 = Customer.objects.create(username='alex_alex')
    customer3 = Customer.objects.create(username='peter132')
    customer4 = Customer.objects.create(username='k.k.')
    customer5 = Customer.objects.create(username='peter_smith')

    # Orders
    order1 = Order.objects.create(customer=customer1)
    order_product1 = OrderProduct.objects.create(order=order1, product=product3, quantity=2)
    order_product2 = OrderProduct.objects.create(order=order1, product=product6, quantity=1)
    order_product3 = OrderProduct.objects.create(order=order1, product=product7, quantity=5)
    order_product4 = OrderProduct.objects.create(order=order1, product=product13, quantity=1)

    order2 = Order.objects.create(customer=customer3)
    order_product5 = OrderProduct.objects.create(order=order2, product=product3, quantity=2)
    order_product6 = OrderProduct.objects.create(order=order2, product=product9, quantity=1)

    order3 = Order.objects.create(customer=customer1)
    order_product5 = OrderProduct.objects.create(order=order3, product=product12, quantity=4)
    order_product6 = OrderProduct.objects.create(order=order3, product=product7, quantity=3)
    return "All data entered!"


# Run and print your queries
# print(add_records_to_database())

# print('All Products:')
# print(Product.objects.all())
# print()
# print('All Available Products:')
# print(Product.objects.available_products())
# print()
# print('All Available Food Products:')
# print(Product.objects.available_products_in_category("Food"))

def product_quantity_ordered():
    products = (Product.objects.annotate(num_orders=Sum('order_product__quantity'))
                .filter(num_orders__gte=1)
                .order_by('-num_orders'))

    return '\n'.join(
        f'Quantity ordered of {p.name}: {p.num_orders}'
        for p in products
    )


def ordered_products_per_customer():
    orders = Order.objects.order_by('id')
    result = []
    for o in orders:
        result.append(f'Order ID: {o.id}, Customer: {o.customer.username}')
        for p in o.products.all():
            result.append(f'- Product: {p.name}, Category: {p.category.name}')

    return '\n'.join(result)

#print(ordered_products_per_customer())


def filter_products():
    products = (Product.objects.available_products().
                filter(price__gt=3).
                order_by('-price', 'name'))

    return '\n'.join(
        f'{p.name}: {p.price}lv.'
        for p in products
    )


def give_discount():
    Product.objects.available_products().filter(price__gt=3).update(price=F('price') * 0.7)

    products = Product.objects.available_products().order_by('-price', 'name')

    return '\n'.join(
        f'{p.name}: {p.price}lv.'
        for p in products
    )


