# Generated by Django 3.0.8 on 2020-12-18 14:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201210_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginaadopcion',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='head_images', verbose_name='Imagen de cabecera'),
        ),
        migrations.AddField(
            model_name='paginablog',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='head_images', verbose_name='Imagen de cabecera'),
        ),
        migrations.AddField(
            model_name='paginacontacto',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='head_images', verbose_name='Imagen de cabecera'),
        ),
        migrations.AddField(
            model_name='paginadonaciones',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='head_images', verbose_name='Imagen de cabecera'),
        ),
        migrations.AddField(
            model_name='paginadonaciones',
            name='info_mp',
            field=ckeditor.fields.RichTextField(default='Actualmente no disponible.', verbose_name='Info de Mercado Pago'),
        ),
        migrations.AddField(
            model_name='paginadonaciones',
            name='info_pp',
            field=ckeditor.fields.RichTextField(default='Actualmente no disponible.', verbose_name='Info de Paypal'),
        ),
        migrations.AddField(
            model_name='paginadonaciones',
            name='mp_qr',
            field=models.ImageField(blank=True, null=True, upload_to='qr', verbose_name='Código QR de Mercado Pago'),
        ),
        migrations.AddField(
            model_name='paginadonaciones',
            name='pp_qr',
            field=models.ImageField(blank=True, null=True, upload_to='qr', verbose_name='Código QR de PayPal'),
        ),
        migrations.AddField(
            model_name='paginainicio',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='head_images', verbose_name='Imagen de cabecera'),
        ),
    ]
