import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from django.db.models import Q, Count, Avg

from main_app.models import Author, Article, Review


# Import your models here
# Create and run your queries within functions
def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    q = Q()
    if search_name is None:
        q = Q(email__icontains=search_email)
    elif search_email is None:
        q = Q(full_name__icontains=search_name)
    else:
        q = (Q(email__icontains=search_email) & Q(full_name__icontains=search_name))

    authors = Author.objects.filter(q).order_by('-full_name')
    if not authors:
        return ''

    result = []
    for a in authors:
        is_banned = 'Banned' if a.is_banned else 'Not Banned'
        result.append(f'Author: {a.full_name}, email: {a.email}, status: {is_banned}')

    return '\n'.join(result)


def get_top_publisher():
    authors = Author.objects.get_authors_by_article_count().first()
    if not Article.objects.all():
        return ''
    return f"Top Author: {authors.full_name} with {authors.num_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews', 'email').first()
    if not Review.objects.all():
        return ''

    return f"Top Reviewer: {author.full_name} with {author.num_reviews} published reviews."


def get_latest_article():
    if not Article.objects.all():
        return ''

    article = (Article.objects.annotate(num_reviews=Count('reviews'), avg_rating=Avg('reviews__rating'))
               .order_by('-published_on').first())

    if not Review.objects.all() or not article.reviews.all():
        return ''

    authors = ', '.join([a.full_name for a in article.authors.order_by('full_name')])

    return (f"The latest article is: {article.title}."
            f" Authors: {authors}. Reviewed: {article.num_reviews} times."
            f" Average Rating: {article.avg_rating:.02f}.")


def get_top_rated_article():
    if not Review.objects.all():
        return ''
    articles = (Article.objects.annotate(num_reviews=Count('reviews'), av_rating=Avg('reviews__rating'))
                .order_by('-av_rating', 'title').first())

    return (f"The top-rated article is: {articles.title}, "
            f"with an average rating of {articles.av_rating:.02f},"
            f" reviewed {articles.num_reviews} times.")


def ban_author(email=None):
    if email is None or not Author.objects.all():
        return "No authors banned."

    author = Author.objects.filter(email=email).first()
    if not author:
        return "No authors banned."

    author.is_banned = True
    author.save()
    counter = 0
    for r in author.reviews.all():
        r.delete()
        counter += 1

    return f"Author: {author.full_name} is banned! {counter} reviews deleted."

