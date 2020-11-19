from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='structure'),
    path('structure/<int:branch_id>/', view_branch, name="view_branch"),
]
