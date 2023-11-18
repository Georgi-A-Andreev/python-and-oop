import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from django.db.models import Q, Count, Avg, F
from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    search_name_query = Q(full_name__icontains=search_name)
    search_nationality_query = Q(nationality__icontains=search_nationality)
    query = None
    if search_name and search_nationality:
        query = search_nationality_query & search_name_query
    elif search_name:
        query = search_name_query
    else:
        query = search_nationality_query

    directors = Director.objects.filter(query).order_by('full_name')
    if not directors:
        return ''

    return '\n'.join([f'Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}'
                      for d in directors])


def get_top_director():
    director = Director.objects.annotate(sum_movies=Count('movies')).order_by('-sum_movies', 'full_name').first()
    if not director:
        return ''

    return f'Top Director: {director.full_name}, movies: {director.sum_movies}.'


def get_top_actor():
    actor = Actor.objects.annotate(sum_movies=Count('movies'), avg_rating=Avg('movies__rating')).order_by('-sum_movies', 'full_name').first()
    if not Movie.objects.all() or not actor:
        return ''

    return (f'Top Actor: {actor.full_name}, starring in movies: {", ".join([t.title for t in actor.movies.all()])},'
            f' movies average rating: {actor.avg_rating:.01f}')


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(sum_movies=Count('movies_many')).order_by('-sum_movies', 'full_name')[:3]

    if not actors or actors[0].sum_movies == 0:
        return ''

    return '\n'.join(f'{a.full_name}, participated in {a.sum_movies} movies'
                     for a in actors)


def get_top_rated_awarded_movie():
    movies = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()
    if not movies:
        return ''
    starring_actor = movies.starring_actor.full_name if movies.starring_actor else 'N/A'
    cast = ', '.join([a.full_name for a in movies.actors.order_by('full_name')])

    return (f"Top rated awarded movie: {movies.title}, rating: {movies.rating:.1f}."
            f" Starring actor: {starring_actor}. "
            f"Cast: {cast}.")


def increase_rating():
    movies = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies:
        return f"No ratings increased."

    update = movies.update(rating=F('rating') + 0.1)
    return f"Rating increased for {update} movies."
