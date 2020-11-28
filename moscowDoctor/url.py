from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='moscowDoctor'),
    path('<int:doctor_id>/', view_doctor, name="view_doctor"),
]
