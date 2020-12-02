from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class RegularPage(models.Model):
    title = models.CharField(max_length=500, verbose_name='Наименование')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('regular_pages_detail', kwargs={"regular_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статическую страницу'
        verbose_name_plural = 'Статические страницы'
