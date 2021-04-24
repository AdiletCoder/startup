from django.shortcuts import render, get_object_or_404
from .models import Measurement


app_name = 'tests'


def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    context = {'distance': obj}
    return render(request, 'main.html', context)
