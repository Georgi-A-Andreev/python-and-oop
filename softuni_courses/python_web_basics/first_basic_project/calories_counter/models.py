from django.core.validators import MinValueValidator
from django.db import models


class Foods(models.Model):
    name = models.CharField(max_length=100)
    protein = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    carbs = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    fats = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    total_calories = models.DecimalField(max_digits=7, decimal_places=1, default=0)


class Activities(models.Model):
    name = models.CharField(max_length=100)
    calories_per_hour = models.IntegerField()


class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    total_calories_to_burn = models.DecimalField(max_digits=10, decimal_places=1, default=0)
