# Generated by Django 3.0.8 on 2020-12-01 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='publicado',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
    ]
