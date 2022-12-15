from django.db import models

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    f_nacimiento = models.IntegerField()
    numero_pasaporte = models.IntegerField()
    edad = models.IntegerField()
   
    
    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.f_nacimiento}, {self.numero_pasaporte},  {self.edad}, {self.id}"

class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    procedencia = models.CharField(max_length=100)
    ingredientes = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.procedencia}, {self.ingredientes}, {self.id}"

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    

     





 

