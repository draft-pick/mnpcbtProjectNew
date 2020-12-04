from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='needToKnow'),
    path('<int:know_id>/', view_know, name="view_know"),
]
