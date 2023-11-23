import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, Avg

from main_app.models import Director, Actor, Movie


# Import your models here
# Create and run your queries within functions

# print(Director.objects.get_directors_by_movies_count())
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    q = Q()
    if search_nationality is None:
        q = Q(full_name__icontains=search_name)
    elif search_name is None:
        q = Q(nationality__icontains=search_nationality)
    else:
        q = (Q(nationality__icontains=search_nationality) & Q(full_name__icontains=search_name))

    directors = Director.objects.filter(q).order_by('full_name')
    if not directors:
        return ''

    return '\n'.join(
        f'Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}'
        for d in directors
    )


def get_top_director():
    s_actor = Director.objects.annotate(num_movies=Count('movies')).order_by('-num_movies', 'full_name').first()
    if not s_actor:
        return ''

    return f"Top Director: {s_actor.full_name}, movies: {s_actor.num_movies}."


def get_top_actor():
    actor = Actor.objects.annotate(num_movies=Count('movies'), avg_rating=Avg('movies__rating')).order_by('-num_movies', 'full_name').first()

    if not Movie.objects.all() or not actor:
        return ''
    movies = ', '.join([m.title for m in actor.movies.all()])

    return (f'Top Actor: {actor.full_name}, starring in movies: {movies},'
            f' movies average rating: {actor.avg_rating:.1f}')


