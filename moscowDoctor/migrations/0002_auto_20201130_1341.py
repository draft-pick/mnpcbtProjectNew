# Generated by Django 3.0.9 on 2020-11-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moscowDoctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='slogan',
            field=models.CharField(blank=True, max_length=500, verbose_name='Слоган'),
        ),
    ]
