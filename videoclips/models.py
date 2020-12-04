from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Video(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    image_title = models.ImageField(upload_to='video', verbose_name='Фото обложки', blank=True)

    def get_absolute_url(self):
        return reverse('view_video', kwargs={"video_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеоролик'
        verbose_name_plural = 'Видеоролики'




