from django.shortcuts import render
from .models import *


def index(request):
    know = Know.objects.all()
    context = {
        'know': know,
        'title': 'Это нужно знать!'
    }
    return render(request, 'needToKnow/index.html', context=context)


def view_know(request, know_id):
    know_item = Know.objects.get(pk=know_id)
    context = {
        'title': know_item.title,
        "know_item": know_item,
    }
    return render(request, 'needToKnow/view_know.html', context=context)