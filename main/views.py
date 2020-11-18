from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)
