from django.shortcuts import render
from .models import Iris


def iris_list(request):
    return render(request, 'home.html', {'iris_list': Iris.objects.all()})
