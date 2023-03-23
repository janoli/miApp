from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class CicloLectivo(models.Model):
    anio = models.IntegerField(validators=[MinValueValidator(2022)])
    
    def __str__(self):
        return str(self.anio)


class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
#    asiento = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Inscripcion(models.Model):
    ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('ciclo_lectivo', 'alumno', 'curso')