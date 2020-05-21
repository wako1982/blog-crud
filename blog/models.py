from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    poblacion=models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.nombre    
        