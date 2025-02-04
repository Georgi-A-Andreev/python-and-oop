import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, Avg, F

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


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(num_movies=Count('movies_actors')).order_by('-num_movies', 'full_name')[:3]

    if not Movie.objects.all() or not actors:
        return ''

    return '\n'.join(
        f'{a.full_name}, participated in {a.num_movies} movies'
        for a in actors
    )


def get_top_rated_awarded_movie():
    m = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()
    if not m:
        return ''
    s_actor = m.starring_actor.full_name if m.starring_actor is not None else 'N/A'

    return (f'Top rated awarded movie: {m.title},'
            f' rating: {m.rating:.1f}. Starring actor: '
            f'{s_actor}. Cast:'
            f' {", ".join([a.full_name for a in m.actors.all()])}.')


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)
    result = movies_to_update.update(rating=F('rating') + 0.1)
    if result == 0:
        return f"No ratings increased."
    return f'Rating increased for {result} movies.'

