"""mnpcbtProjectNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.url')),
    path('news/', include('news.url')),
    path('articles/', include('articles.url')),
    path('structure/', include('structure.url')),
    path('reviews/', include('reviews.url')),
    path('implink/', include('implink.url')),
    path('moscowDoctor/', include('moscowDoctor.url')),
    path('management/', include('management.url')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('regularPages/', include('regularPages.url')),
    path('needToKnow/', include('needToKnow.url')),
    path('videoclips/', include('videoclips.url')),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)