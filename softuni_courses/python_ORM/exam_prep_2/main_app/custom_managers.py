from django.db import models
from django.db.models import Count


class CustomProfileManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(sum_orders=Count('orders')).filter(sum_orders__gt=2).order_by('-sum_orders')
