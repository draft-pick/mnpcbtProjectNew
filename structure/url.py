from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='structure'),
    path('specialists/', specialists, name='specialists'),
    path('specialists/<int:branch_id>/', view_specialist, name='view_specialist'),
    path('structure/<int:branch_id>/', view_branch, name="view_branch"),
]
