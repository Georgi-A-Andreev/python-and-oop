import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name,
                            origin=origin,
                            age=age,
                            description=description,
                            is_magical=is_magical)

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    result = []
    for l in Location.objects.all().order_by('-id'):
        result.append(f"{l.name} has a population of {l.population}!")

    return '\n'.join(result)


def new_capital():
    capital = Location.objects.first()

    capital.is_capital = True
    capital.save()


def get_capitals():
    result = Location.objects.filter(is_capital=True).values('name')
    return result


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    for c in Car.objects.all():
        discount = sum([int(x) for x in str(c.year)]) / 100
        c.price_with_discount = float(c.price) * (1 - discount)
        c.save()


def get_recent_cars():
    result = []
    for c in Car.objects.filter(year__gte=2020).values('model', 'price_with_discount'):
        result.append(c)

    return result


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    result = []

    tasks = Task.objects.filter(is_finished=False)
    for t in tasks:
        result.append(f"Task - {t.title} needs to be done until {t.due_date}!")

    return '\n'.join(result)


def complete_odd_tasks():

    for t in Task.objects.all():
        if t.id % 2 == 1:
            t.is_finished = True
            t.save()


def encode_and_replace(text: str, task_title: str):

    encoded_text = ''
    for c in text:
        encoded_text += chr(ord(c) - 3)

    for t in Task.objects.all():
        if t.title == task_title:
            t.description = encoded_text
            t.save()


def get_deluxe_rooms():
    result = []
    for r in HotelRoom.objects.filter(room_type='Deluxe'):
        if r.id % 2 == 0:
            result.append(f"Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!")

    return '\n'.join(result)


def increase_room_capacity():
    increase = None
    for r in HotelRoom.objects.all():
        if not r.is_reserved:
            continue
        elif increase:
            r.capacity += increase
        else:
            r.capacity += r.id

        increase = r.capacity
        r.save()


def reserve_first_room():

    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():

    for r in HotelRoom.objects.order_by('-id'):
        if r.is_reserved:
            r.delete()
            break

