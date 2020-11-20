from django.shortcuts import render
from .models import *
from news.models import News, GalleryNews


def index(request):
    news = News.objects.order_by("-id")[0:4]
    image = GalleryNews.objects.filter(in_the_title=1)
    context = {
        'news': news,
        'image': image,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)
