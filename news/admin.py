from django.contrib import admin

from .models import *


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = GalleryNews


@admin.register(News)
class PostsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
    list_display = ('title', 'created_at', 'anons')
    list_display_links = ('title', 'created_at', 'anons')
    search_fields = ('title', 'anons', 'content')
