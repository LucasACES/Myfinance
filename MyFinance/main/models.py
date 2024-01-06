from django.db import models

# Create your models here.

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=100)