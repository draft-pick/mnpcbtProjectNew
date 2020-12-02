from django.shortcuts import render
from .models import *


def index(request):
    regular = RegularPage.objects.all()
    context = {
        'regular': regular,
        'title': 'Статические страницы',
    }
    return render(request, 'regularPages/index.html', context=context)


def regular_pages_detail(request, regular_id):
    regular_item = RegularPage.objects.get(pk=regular_id)
    context = {
        'title': regular_item.title,
        "regular_item": regular_item,
    }
    return render(request, 'regularPages/regular_detail.html', context=context)
