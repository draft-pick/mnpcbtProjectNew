from django.contrib import admin

from .models import *


@admin.register(Doctors)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    list_display_links = ('title', 'position')
    search_fields = ('title', 'position')
