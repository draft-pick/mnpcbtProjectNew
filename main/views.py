from django.shortcuts import render
from .models import *
from news.models import News, GalleryNews
from structure.models import Branches, GalleryBranches


def index(request):
    news = News.objects.order_by("-id")[0:5]
    image = GalleryNews.objects.filter(in_the_title=1)
    branches = Branches.objects.all()
    image_branches = GalleryBranches.objects.filter(in_the_cont=1)
    context = {
        'news': news,
        'image': image,
        'branches': branches,
        'image_branches': image_branches,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)
