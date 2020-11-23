from django.shortcuts import render
from .models import *


def index(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
        'title': 'Отзывы пациентов'
    }
    return render(request, 'reviews/index.html', context=context)
