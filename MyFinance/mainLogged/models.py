from django.db import models

# Create your models here.

class Banco(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.FloatField()

