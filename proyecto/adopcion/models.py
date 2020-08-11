from django.db import models

# Create your models here.


class Animal(models.Model):

    class Sexo(models.TextChoices):
        MACHO = 'Macho'
        HEMBRA = 'Hembra'
        INDEFINIDO = 'Indefinido'


    class Tamaño(models.TextChoices):
        GRANDE = 'Grande'
        MEDIANO = 'Mediano'
        CHICO = 'Chico'


    class TipoAnimal(models.TextChoices):
        PERRO = 'Perro'
        GATO = 'Gato'


    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'


    def __str__(self):
        return self.nombre

    nombre = models.CharField(verbose_name='Nombre', max_length=255, null=False, blank=False)
    tipo_animal = models.CharField(verbose_name='Tipo de animal', max_length=40, choices=TipoAnimal.choices, null=False, blank=False)
    raza = models.CharField(verbose_name='Raza', max_length=255, null=False, blank=False)
    tamaño = models.CharField(verbose_name='Tamaño', max_length=40, choices=Tamaño.choices, null=False, blank=False)
    # foto1 = models.ImageField()   Configurar Pillow
    # foto2 = models.ImageField()   Configurar Pillow
    edad = models.IntegerField(verbose_name='Edad', null=False, blank=False)
    sexo = models.CharField(verbose_name='Sexo', max_length=40, choices=Sexo.choices, null=False, blank=False)
    caracter = models.TextField(verbose_name='Caracter', null=True, blank=True)
    vacunado = models.BooleanField(verbose_name='Vacunado', null=False, blank=False)
    desparasitado = models.BooleanField(verbose_name='Desparacitado', null=False, blank=False)
    castrado = models.BooleanField(verbose_name='Castrado', null=False, blank=False)
    comentario = models.TextField(verbose_name='Comentarios', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Ultima actualizacion')



