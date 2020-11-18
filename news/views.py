from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Наши новости',
    }
    return render(request, 'news/index.html', context=context)


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    context = {
        'title': news_item.title,
        "news_item": news_item,
    }
    return render(request, 'news/view_news.html', context=context)

