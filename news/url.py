from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='news'),
    path('<int:news_id>/', view_news, name="view_news"),
]
