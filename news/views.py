from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    image = GalleryNews.objects.filter(in_the_title=1)
    context = {
        'news': news,
        'image': image,
        'title': 'Наши новости',
    }
    return render(request, 'news/index.html', context=context)


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    image_title = GalleryNews.objects.all().filter(in_the_title=1, product_id=news_id)
    image = GalleryNews.objects.all().filter(product_id=news_id)
    context = {
        'title': news_item.title,
        "news_item": news_item,
        'image': image,
        'image_title': image_title
    }
    return render(request, 'news/view_news.html', context=context)
