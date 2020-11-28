from django.shortcuts import render
from .models import *


def index(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
        'title': 'Московский врач',
    }
    return render(request, 'moscowDoctor/index.html', context=context)


def view_doctor(request, doctor_id):
    doctor_item = Doctors.objects.get(pk=doctor_id)
    context = {
        'title': doctor_item.title,
        "doctor_item": doctor_item,
    }
    return render(request, 'moscowDoctor/view_doctor.html', context=context)
