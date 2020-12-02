from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='regularPages'),
    path('<int:regular_id>/', regular_pages_detail, name="regular_pages_detail"),
]