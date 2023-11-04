import os
from datetime import timedelta, date

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Book, Artist, Song, Review, Product, DrivingLicense, Driver, Registration, Car


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by('id')

    result = []

    for a in authors:
        books = a.book_set.all()
        if not books:
            continue
        titles = ', '.join(b.title for b in books)
        result.append(f"{a.name} has written - {titles}!")

    return '\n'.join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    count = len(reviews)
    total = sum(r.rating for r in reviews)

    return total / count


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    dl = DrivingLicense.objects.all().order_by("-license_number")

    return '\n'.join(str(d) for d in dl)


def get_drivers_with_expired_licenses(due_date):
    expiration_cutoff_date = due_date - timedelta(days=365)

    expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_cutoff_date)

    return expired_drivers


def register_car_by_owner(owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."