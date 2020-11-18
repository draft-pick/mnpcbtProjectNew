from django.db import models
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField


class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    anons = models.TextField(blank=True, verbose_name='Анонс')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"article_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class GalleryPosts(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    product = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='images')
    in_the_title = models.BooleanField(default=False, verbose_name='Заголовок')



