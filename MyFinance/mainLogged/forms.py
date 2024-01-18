from django import forms
from . import models

class AddBank (forms.ModelForm):
    class Meta:
        model = models.Banco
        fields = ['nome', 'saldo']

class Movimento (forms.ModelForm):
    class Meta:
        model = models.Movimentos
        fields = ['movimento', 'valor', 'banco', 'descricao']