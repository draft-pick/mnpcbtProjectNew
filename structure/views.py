from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    branches = Branches.objects.all()
    paginator = Paginator(branches, 10)
    context = {
        'branches': branches,
        'paginator': paginator,
        'title': 'Структура Центра',
    }
    return render(request, 'structure/index.html', context=context)


def view_branch(request, branch_id):
    branches_item = Branches.objects.get(pk=branch_id)
    image = GalleryBranches.objects.all().filter(keyBranches=branch_id)
    image_map = GalleryBranches.objects.all().filter(location_map=1, keyBranches=branch_id)
    specialists = Specialists.objects.all().filter(keyBranches=branch_id)
    paginator_spec = Paginator(specialists, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator_spec.page(page)
    except PageNotAnInteger:
        contacts = paginator_spec.page(1)
    except EmptyPage:
        contacts = paginator_spec.page(paginator_spec.num_pages)
    return render(request, 'structure/view_branches.html', {'branches_item': branches_item,
                                                            'title': branches_item.name,
                                                            'image': image,
                                                            'image_map': image_map,
                                                            "specialists": specialists,
                                                            "contacts": contacts})

