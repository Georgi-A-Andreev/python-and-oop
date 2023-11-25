import os
import django
# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions

from django.db.models import Q, Count, F

from main_app.models import Profile, Order, Product


def get_profiles(search_string=None):
    if search_string is None:
        return ''
    profile = Profile.objects.filter(Q(full_name__icontains=search_string) |
                                     Q(email__icontains=search_string) |
                                     Q(phone_number__icontains=search_string)).order_by('full_name')

    if not profile:
        return ''

    return '\n'.join(
        f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}'
        for p in profile
    )


def get_loyal_profiles():
    profiles = Profile.objects.annotate(num_orders=Count('orders')).filter(num_orders__gt=2).order_by('-num_orders')
    if not profiles:
        return ''

    return '\n'.join(
        f'Profile: {p.full_name}, orders: {p.num_orders}'
        for p in profiles
    )


def get_last_sold_products():
    latest_order = Order.objects.order_by('-creation_date').first()
    if not latest_order:
        return ''
    products = latest_order.products.all()
    if not products:
        return ''

    return f"Last sold products: {', '.join([p.name for p in products])}"


def get_top_products():
    if not Order.objects.all():
        return ''
    products = Product.objects.annotate(num_orders=Count('orders')).filter(num_orders__gt=0).order_by('-num_orders', 'name')[:5]

    if not products:
        return ''

    return 'Top products:\n' + '\n'.join(
        f'{p.name}, sold {p.num_orders} times'
        for p in products
    )


def apply_discounts():
    orders = Order.objects.annotate(num_products=Count('products')).filter(num_products__gt=2, is_completed=False)

    result = orders.update(total_price=F('total_price') * 0.9)
    return f"Discount applied to {result} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()
    if not order:
        return ''
    order.is_completed = True
    order.save()

    for p in order.products.all():
        p.in_stock -= 1
        if p.in_stock == 0:
            p.is_available = False
        p.save()

    return "Order has been completed!"