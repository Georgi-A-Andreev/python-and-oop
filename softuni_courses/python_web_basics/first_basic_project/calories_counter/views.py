from django.http import HttpResponse
from django.shortcuts import render

from calories_counter.models import People


def all_people(request):
    output = People.objects.order_by('-total_calories_to_burn')
    result = []
    for p in output:
        result.append(f'{p.name} has {p.total_calories_to_burn} more calories to burn to be fit!')
    context = {'people': result}
    return render(request, 'calories/people.html', context=context)

