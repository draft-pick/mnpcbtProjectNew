from django.shortcuts import render
from .models import *
from news.models import News, GalleryNews
from structure.models import Branches, GalleryBranches
from reviews.models import Reviews


def index(request):
    news = News.objects.order_by("-id")[0:4]
    branches = Branches.objects.all()
    image_branches = Branches.objects.all()
    reviews = Reviews.objects.all()
    context = {
        'news': news,
        'branches': branches,
        'image_branches': image_branches,
        'reviews': reviews,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)
