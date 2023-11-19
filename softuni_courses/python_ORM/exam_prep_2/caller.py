import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, F
from main_app.models import Profile, Product, Order


def get_profiles(search_string=None):
    if search_string is None:
        return ''

    first = Q(full_name__icontains=search_string)
    second = Q(email__icontains=search_string)
    third = Q(phone_number__icontains=search_string)

    profiles = Profile.objects.filter(first | second | third).order_by('full_name')
    if not profiles:
        return ''

    return '\n'.join(
        f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}'
        for p in profiles
        )


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()
    if not profiles:
        return ''

    return '\n'.join(
        f'Profile: {p.full_name}, orders: {p.sum_orders}'
        for p in profiles
    )


def get_last_sold_products():
    latest_order = Order.objects.order_by('-creation_date').first()
    if not latest_order:
        return ''
    products = latest_order.products.all().order_by('name')
    if not products:
        return ''

    return '\n'.join(
        f'Last sold products: {", ".join(p.name for p in products)}'
    )


def get_top_products():
    if not Order.objects.all():
        return ''
    products = Product.objects.annotate(num_orders=Count('orders')).filter(num_orders__gt=0).order_by('-num_orders', 'name')[:5]
    if not products:
        return ''
    result = ['Top products:']
    for p in products:
        result.append(f'{p.name}, sold {p.num_orders} times')

    return '\n'.join(result)


def apply_discounts():
    orders = (Order.objects.annotate(num_products=Count('products')).
              filter(num_products__gt=2, is_completed=False).
              update(total_price=F('total_price') * 0.9))

    return f"Discount applied to {orders} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()
    if not order:
        return ''
    order.is_completed = True
    order.save()
    products = order.products.all()
    if not products:
        return ''
    for p in products:
        p.in_stock -= 1
        if p.in_stock <= 0:
            p.is_available = False
        p.save()
    return "Order has been completed!"
