from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Know(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    content = RichTextUploadingField(blank=True, verbose_name='Текст')

    def get_absolute_url(self):
        return reverse('view_know', kwargs={"know_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Это нужно знать'
        verbose_name_plural = 'Это нужно знать'
        ordering = ['title']
