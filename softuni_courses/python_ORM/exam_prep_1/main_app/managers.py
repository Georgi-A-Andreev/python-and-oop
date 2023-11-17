from django.db import models
from django.db.models import Count


class CustomManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(c_movies=Count('director_movie__director')).order_by('-c_movies', 'full_name')
