from django.contrib import admin

from calories_counter.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_calories_to_burn')


