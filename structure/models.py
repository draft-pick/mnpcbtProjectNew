from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Branches(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    contacts = RichTextUploadingField(blank=True, verbose_name='Контактная информация')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    image_title = models.ImageField(upload_to='branches/', verbose_name='Фото заголовка', blank=True)

    def get_absolute_url(self):
        return reverse('view_branch', kwargs={"branch_id": self.pk})

    def get_spec_url(self):
        return reverse('view_specialist', kwargs={"branch_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class GalleryBranches(models.Model):
    image = models.ImageField(upload_to='branches/', verbose_name='Фото/Схема проезда', blank=True)
    keyBranches = models.ForeignKey(Branches, on_delete=models.CASCADE, related_name='images')
    location_map = models.BooleanField(default=False, verbose_name='Схема проезда')


class Specialists(models.Model):
    keyBranches = models.ForeignKey(Branches, on_delete=models.CASCADE, related_name='specialist', verbose_name='Филиал')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(blank=True, max_length=100, verbose_name='Отчество')
    division = models.CharField(blank=True, max_length=300, verbose_name='Подразделение (Наименование)')
    job = models.CharField(blank=True, max_length=200, verbose_name='Штатная должность (Наименование)')
    vyz = models.CharField(blank=True, max_length=300, verbose_name='ВУЗ')
    date_vyz = models.CharField(blank=True, max_length=100, verbose_name='Дата окончания')
    profession = models.CharField(blank=True, max_length=200, verbose_name='Специальность')
    sertif = models.CharField(blank=True, max_length=100, verbose_name='Сертификат')
    date_sertif = models.CharField(blank=True, max_length=100, verbose_name='Дата выдачи')
    category = models.CharField(blank=True, max_length=100, verbose_name='Категория')
    degree = models.CharField(blank=True, max_length=100, verbose_name='Степень')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'



