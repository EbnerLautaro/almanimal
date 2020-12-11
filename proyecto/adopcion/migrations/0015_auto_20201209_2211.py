# Generated by Django 3.0.8 on 2020-12-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0014_auto_20201209_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='raza_gato',
            field=models.CharField(choices=[('', 'Blank'), ('Mestizo', 'Mestizo'), ('Americano de pelo corto', 'Americano Pelo Corto'), ('Angora Turco', 'Angora Turco'), ('Azul Ruso', 'Azul Ruso'), ('Bengali', 'Bengali'), ('Bombay', 'Bombay'), ('British Shorthair', 'British Shorthair'), ('Europeo de pelo corto', 'Europeo Pelo Corto'), ('Persa', 'Persa'), ('Sagrado de Birmania', 'Sagrado Birmania'), ('Siames', 'Siames'), ('Snowshoe', 'Snowshoe')], help_text='Dejar en blanco si es Perro', max_length=30, verbose_name='Raza Gato'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='raza_perro',
            field=models.CharField(choices=[('', 'Blank'), ('Mestizo', 'Mestizo'), ('Akita Inu', 'Akita Inu'), ('Basset Hound o Batata', 'Batata'), ('Beagle', 'Beagle'), ('Bichon Frise', 'Bichon Frise'), ('Border Collie', 'Border Collie'), ('Boxer', 'Boxer'), ('Braco Aleman Kurzhaar', 'Braco Aleman'), ('Braco hungaro o Vizsla', 'Braco Hungaro'), ('Breton', 'Breton'), ('Bull Terrier', 'Bull Terrier'), ('Bulldog Frances', 'Bulldog Fr'), ('Bulldog Ingles', 'Bulldog In'), ('Caniche', 'Caniche'), ('Chihuahua', 'Chihuahua'), ('Chow Chow', 'Chow Chow'), ('Cocker Spaniel', 'Cocker'), ('Collie', 'Collie'), ('Dachshund o Salchicha', 'Salchicha'), ('Dalmata', 'Dalmata'), ('Doberman', 'Doberman'), ('Dogo Argentino', 'Dogo Arg'), ('Dogo de Burdeos', 'Dobo Burd'), ('Fox Terrier', 'Fox Terrier'), ('Galgo', 'Galgo'), ('Golden Retriever', 'Golden'), ('Gran Danes', 'Gran Danes'), ('Jack Russell Terrier', 'Jack Russell'), ('Labrador Retriever', 'Labrador'), ('Lhasa Apso', 'Lhasa'), ('Maltes', 'Maltes'), ('Mastin Napolitano', 'Mastin'), ('Ovejero Aleman', 'Ovejero'), ('Pastor Belga', 'Pastor Bg'), ('Pastor Ingles', 'Pastor In'), ('Pekines', 'Pekines'), ('Pila', 'Pila'), ('Pinscher', 'Pinscher'), ('Pitbull', 'Pitbull'), ('Pointer', 'Pointer'), ('Presa Canario', 'Presa Canario'), ('Pug/Carlino', 'Pug'), ('Rottweiler', 'Rottweiler'), ('Samoyedo', 'Samoyedo'), ('San Bernardo', 'San Bernardo'), ('Schnauzer', 'Schnauzer'), ('Setter Irlandes', 'Setter'), ('Shar Pei', 'Shar Pei'), ('Shiba Inu', 'Shiba Inu'), ('Shih TzuHusky Siberiano', 'Shih'), ('Weimaraner', 'Weimaraner'), ('Whippet', 'Whippet'), ('Yorkshire Terrier', 'Yorkshire')], help_text='Dejar en blanco si es Gato', max_length=30, verbose_name='Raza Perro'),
        ),
    ]