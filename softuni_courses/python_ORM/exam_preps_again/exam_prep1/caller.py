import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Director
# Import your models here
# Create and run your queries within functions

# print(Director.objects.get_directors_by_movies_count())
