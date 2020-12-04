from django.shortcuts import render
from .models import *


def index(request):
    videoclips = Video.objects.all()
    context = {
        'videoclips': videoclips,
        'title': 'Видеоролики',
    }
    return render(request, 'videoclips/index.html', context=context)


def view_video(request, video_id):
    video_item = Video.objects.get(pk=video_id)
    context = {
        'title': video_item.title,
        "video_item": video_item,
    }
    return render(request, 'videoclips/view_video.html', context=context)
