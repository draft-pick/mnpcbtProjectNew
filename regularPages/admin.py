from django.contrib import admin

from .models import *


@admin.register(RegularPage)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
