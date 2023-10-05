from django.db import models

##declaracion de clases 
class courses(models.Model):
    nivel = models.CharField(max_length=20)
    
class in_companyTraining(models.Model):
    nivel = models.CharField(max_length=20)
    
class team(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField(max_length=8)
    
