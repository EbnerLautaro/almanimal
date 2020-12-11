# Generated by Django 3.0.8 on 2020-12-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0020_auto_20201210_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='raza_gato',
            field=models.CharField(blank=True, choices=[('Mestizo', 'Mestizo'), ('Americano De Pelo Corto', 'Americano De Pelo Corto'), ('Angora Turco', 'Angora Turco'), ('Azul Ruso', 'Azul Ruso'), ('Bengali', 'Bengali'), ('Bombay', 'Bombay'), ('British Shorthair', 'British Shorthair'), ('Europeo De Pelo Corto', 'Europeo De Pelo Corto'), ('Persa', 'Persa'), ('Sagrado De Birmania', 'Sagrado De Birmania'), ('Siames', 'Siames'), ('Snowshoe', 'Snowshoe')], help_text='Dejar en blanco si es Perro u Otro', max_length=30, null=True, verbose_name='Raza Gato'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='raza_perro',
            field=models.CharField(blank=True, choices=[('Mestizo', 'Mestizo'), ('Akita Inu', 'Akita Inu'), ('Basset Hound O Batata', 'Basset Hound O Batata'), ('Beagle', 'Beagle'), ('Bichon Frise', 'Bichon Frise'), ('Border Collie', 'Border Collie'), ('Boxer', 'Boxer'), ('Braco Aleman Kurzhaar', 'Braco Aleman Kurzhaar'), ('Braco hungaro O Vizsla', 'Braco Hungaro O Vizsla'), ('Breton', 'Breton'), ('Bull Terrier', 'Bull Terrier'), ('Bulldog Frances', 'Bulldog Frances'), ('Bulldog Ingles', 'Bulldog Ingles'), ('Caniche', 'Caniche'), ('Chihuahua', 'Chihuahua'), ('Chow Chow', 'Chow Chow'), ('Cocker Spaniel', 'Cocker Spaniel'), ('Collie', 'Collie'), ('Dachshund O Salchicha', 'Dachshund O Salchicha'), ('Dalmata', 'Dalmata'), ('Doberman', 'Doberman'), ('Dogo Argentino', 'Dogo Argentino'), ('Dogo de Burdeos', 'Dogo De Burdeos'), ('Fox Terrier', 'Fox Terrier'), ('Galgo', 'Galgo'), ('Golden Retriever', 'Golden Retriever'), ('Gran Danes', 'Gran Danes'), ('Jack Russell Terrier', 'Jack Russell Terrier'), ('Labrador Retriever', 'Labrador Retriever'), ('Lhasa Apso', 'Lhasa Apso'), ('Maltes', 'Maltes'), ('Mastin Napolitano', 'Mastin Napolitano'), ('Ovejero Aleman', 'Ovejero Aleman'), ('Pastor Belga', 'Pastor Belga'), ('Pastor Ingles', 'Pastor Ingles'), ('Pekines', 'Pekines'), ('Pila', 'Pila'), ('Pinscher', 'Pinscher'), ('Pitbull', 'Pitbull'), ('Pointer', 'Pointer'), ('Presa Canario', 'Presa Canario'), ('Pug', 'Pug'), ('Rottweiler', 'Rottweiler'), ('Samoyedo', 'Samoyedo'), ('San Bernardo', 'San Bernardo'), ('Schnauzer', 'Schnauzer'), ('Setter Irlandes', 'Setter Irlandes'), ('Shar Pei', 'Shar Pei'), ('Shiba Inu', 'Shiba Inu'), ('Shih TzuHusky Siberiano', 'Shih Tzuhusky Siberiano'), ('Weimaraner', 'Weimaraner'), ('Whippet', 'Whippet'), ('Yorkshire Terrier', 'Yorkshire Terrier')], help_text='Dejar en blanco si es Gato u Otro', max_length=30, null=True, verbose_name='Raza Perro'),
        ),
    ]