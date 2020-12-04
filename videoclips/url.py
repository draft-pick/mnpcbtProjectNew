from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='videoclips'),
    path('<int:video_id>/', view_video, name="view_video"),
]
