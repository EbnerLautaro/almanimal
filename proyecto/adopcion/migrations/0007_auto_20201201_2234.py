# Generated by Django 3.0.8 on 2020-12-02 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0006_auto_20201201_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='tiempo',
            field=models.CharField(choices=[('Días', 'Dias'), ('Semanas', 'Semanas'), ('Meses', 'Meses'), ('Años', 'Años')], max_length=50, verbose_name='Tiempo'),
        ),
    ]