from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Management(models.Model):
    title = models.CharField(max_length=300, verbose_name='ФИО')
    position = models.CharField(max_length=500, verbose_name='Должность')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    image_title = models.ImageField(upload_to='management', verbose_name='Фото', blank=True)
    main_card = models.BooleanField(default=False, verbose_name='Директор')

    def get_absolute_url(self):
        return reverse('view_management', kwargs={"management_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Руководство Центра'
        verbose_name_plural = 'Руководство Центра'


class GalleryManagement(models.Model):
    image = models.ImageField(upload_to='management', verbose_name='Фотогаллерея', blank=True)
    product = models.ForeignKey(Management, on_delete=models.CASCADE, related_name='images')
    main_image = models.BooleanField(default=False, verbose_name='Главное фото')


