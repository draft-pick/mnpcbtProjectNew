from django.db import models
from django.urls import reverse


class ImpLink(models.Model):
    content = models.CharField(max_length=500, blank=True, verbose_name='Контент')
    image_title = models.ImageField(upload_to='implink', verbose_name='Изображение', blank=True)
    link = models.CharField(max_length=500, blank=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Важные ссылки'
        verbose_name_plural = 'Важные ссылки'
