from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='articles'),
    path('articles/<int:article_id>/', article_detail, name="article_detail"),
]