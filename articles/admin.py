from django.contrib import admin

from .models import *


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at', 'updated_at', 'is_published')
#     list_display_links = ('title', 'created_at', 'updated_at', 'is_published')
#     search_fields = ('title', 'anons', 'content')

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = GalleryPosts


@admin.register(Articles)
class PostsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
