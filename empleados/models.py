from django.db import models

# Create your models here.


class Departamento(models.Model):    
    nombre=models.TextField(max_length=50)

def __str__(self):
    return self.nombre

class Empleado(models.Model):
    nombre=models.TextField(max_length=100)
    email=models.TextField(max_length=100)
    telefono=models.TextField(max_length=20)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)


