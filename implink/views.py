from django.shortcuts import render
from .models import *


def index(request):
    reviews = ImpLink.objects.all()
    context = {
        'reviews': reviews,
        'title': 'Отзывы пациентов'
    }
    return render(request, 'implink/index.html', context=context)
