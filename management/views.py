from django.shortcuts import render
from .models import *


def index(request):
    management = Management.objects.all()
    main_management = Management.objects.filter(main_card=1)
    context = {
        'management': management,
        'main_management': main_management,
        'title': 'Руководство Центра',
    }
    return render(request, 'management/index.html', context=context)


def view_management(request, management_id):
    management_item = Management.objects.get(pk=management_id)
    context = {
        'title': management_item.title,
        "management_item": management_item,
    }
    return render(request, 'management/view_management.html', context=context)
