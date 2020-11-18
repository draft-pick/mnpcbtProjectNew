from django.shortcuts import render
from .models import *


def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles,
        'title': 'Наши статьи',
    }
    return render(request, 'articles/index.html', context=context)


def article_detail(request, article_id):
    article_item = Articles.objects.get(pk=article_id)
    context = {
        'title': article_item.title,
        "article_item": article_item,
    }
    return render(request, 'articles/article_detail.html', context=context)