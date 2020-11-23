from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    image = GalleryNews.objects.all()
    context = {
        'news': news,
        'image': image,
        'title': 'Наши новости',
    }
    return render(request, 'news/index.html', context=context)


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    images_gallery = GalleryNews.objects.all().filter(product_id=news_id)
    context = {
        'title': news_item.title,
        "news_item": news_item,
        'images_gallery': images_gallery,
    }
    return render(request, 'news/view_news.html', context=context)
