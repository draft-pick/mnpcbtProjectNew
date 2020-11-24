from django.contrib import admin

from .models import *


class ReviewsAdmin(admin.ModelAdmin):
    list_display = 'content'
    list_display_links = 'content'
    search_fields = 'content'


admin.site.register(ImpLink)
