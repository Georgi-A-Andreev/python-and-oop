import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    directors = None
    if search_nationality is None and search_name is None:
        return ''

    if search_nationality is not None and search_name is not None:
        directors = Director.objects.filter(Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality))

    elif search_nationality is None:
        directors = Director.objects.filter(full_name__icontains=search_name)

    elif search_nationality is not None:
        directors = Director.objects.filter(nationality__icontains=search_nationality)

    if not directors:
        return ''

    return '\n'.join(
        f'Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}'
        for d in directors.order_by('full_name')
    )


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ''

    return f'Top Director: {director.full_name}, movies: {director.c_movies}.'


def get_top_actor():
    actor = (Actor.objects.prefetch_related('movies')
             .annotate(max_movies=Count('actor_movie__starring_actor'), av_rating=Avg('actor_movie__rating'))
             .order_by('-max_movies', 'full_name').first())
    if not actor:
        return ''

    movies = Movie.objects.filter(starring_actor=actor.id)
    if not movies:
        return ''

    return (f"Top Actor: {actor.full_name},"
            f" starring in movies:"
            f" {', '.join(t.title for t in movies)}, movies average rating: {actor.av_rating}")
