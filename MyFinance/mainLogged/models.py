from django.db import models

# Create your models here.

class Banco(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    saldo = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.nome

class Movimentos(models.Model):
    tipo = (('E', 'Entrada'),('S', 'Saída'))
    movimento = models.CharField(max_length=1, choices=tipo, default=None, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False, default=0)
    banco = models.ForeignKey(Banco, default=None, blank=False, null=False, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(max_length = 250, default=None)