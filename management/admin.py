from django.contrib import admin

from .models import *


class GalleryInline(admin.TabularInline):
    man_name = 'product'
    model = GalleryManagement


@admin.register(Management)
class PostsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
    list_display = ('title', 'position')
    list_display_links = ('title', 'position')
    search_fields = ('title', 'position')
