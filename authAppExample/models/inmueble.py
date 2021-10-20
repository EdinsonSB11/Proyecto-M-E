from django.db import models
from .user     import User
from django.utils import timezone

class Account(models.Model):
    id             = models.AutoField(primary_key=True)
    habitaciones   = models.IntegerField(default=0)
    banios         = models.IntegerField(default=0)
    alimentacion   = models.BooleanField(default=True)      
    valoracion     = models.IntegerField(default=0.0)
    precio         = models.IntegerField(default=0)
    descripcion    = models.CharField('Descripcion inmueble', max_length=50,default='')
    ubicacion      = models.CharField('Ubicacion inmueble', max_length=50,default='')
    lastChangeDate = models.DateField(default=timezone.now)
    isAvailable    = models.BooleanField(default=True)

    def _str_(self):
        return self.descripcion