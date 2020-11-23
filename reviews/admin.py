from django.contrib import admin

from .models import *


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_display_links = ('name', 'date')
    search_fields = ('name', 'date', 'content')


admin.site.register(Reviews)
