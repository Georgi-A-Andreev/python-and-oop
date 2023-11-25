import os
import django
# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions

from django.db.models import Q, Count

from main_app.models import Profile, Order


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
