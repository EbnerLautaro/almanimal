# Generated by Django 3.0.8 on 2020-11-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_auto_20201112_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email de contacto'),
        ),
        migrations.AddField(
            model_name='animal',
            name='telefono',
            field=models.CharField(default='', max_length=50, verbose_name='Teléfono de contacto'),
        ),
    ]
