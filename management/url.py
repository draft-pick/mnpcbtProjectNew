from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='management'),
    path('<int:management_id>/', view_management, name="view_management"),
]
