from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown')
    years_of_experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])


class Actor(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown')
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    choices = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other')
    ]
    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=6, default='Other', choices=choices)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0,
                                 validators=[MinValueValidator(0), MaxValueValidator(10.0)])
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    starring_actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, blank=True, null=True, related_name='Actors')
    actors = models.ManyToManyField(Actor)
