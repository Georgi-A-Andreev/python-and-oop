import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from django.db.models import Q, Count

from main_app.models import Author
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

    authors = Author.objects.filter(q)
    if not authors:
        return ''

    result = []
    for a in authors:
        is_banned = 'Banned' if a.is_banned else 'Not Banned'
        result.append(f'Author: {a.full_name}, email: {a.email}, status: {is_banned}')

    return '\n'.join(result)


def get_top_publisher():
    authors = Author.objects.get_authors_by_article_count().first()
    if not authors:
        return ''

    return f"Top Author: {authors.full_name} with {authors.num_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews', 'email').first()
    if not author:
        return ''

    return f"Top Reviewer: {author.full_name} with {author.num_reviews} published reviews."
