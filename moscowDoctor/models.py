from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Doctors(models.Model):
    title = models.CharField(max_length=300, verbose_name='ФИО')
    position = models.CharField(max_length=500, verbose_name='Должность')
    slogan = models.CharField(blank=True, max_length=500, verbose_name='Слоган')
    education = RichTextUploadingField(blank=True, verbose_name='Образование')
    working_activity = RichTextUploadingField(blank=True, verbose_name='Трудовая деятельность')
    additionally = RichTextUploadingField(blank=True, verbose_name='Дополнительные сведения о кандидате')
    image = models.ImageField(upload_to='doctors', verbose_name='Фото', blank=True)

    def get_absolute_url(self):
        return reverse('view_doctor', kwargs={"doctor_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Московский врач'
        verbose_name_plural = 'Московский врач'





