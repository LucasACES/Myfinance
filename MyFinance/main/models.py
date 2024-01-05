from django.db import models

# Create your models here.
class Banco(models.Model):
    nome = models.CharField(max_length=30)
    saldo = models.FloatField()

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=100)