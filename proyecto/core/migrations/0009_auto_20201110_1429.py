# Generated by Django 3.0.8 on 2020-11-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201110_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
