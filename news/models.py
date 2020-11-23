from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    anons = models.TextField(blank=True, verbose_name='Анонс')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    image_title = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class GalleryNews(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    product = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')




