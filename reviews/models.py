from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Reviews(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    content = RichTextUploadingField(blank=True, verbose_name='Текст')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['date']
