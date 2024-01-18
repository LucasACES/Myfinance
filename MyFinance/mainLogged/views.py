from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def homeLogged(request):
    saldoSomado = 0
    bancoSaldo = models.Banco.objects.all()
    for banco in bancoSaldo:
        saldoSomado = banco.saldo + saldoSomado
    return render(request, 'html/home.html', {'saldo': saldoSomado})

def bankLogged(request):
    banco = models.Banco.objects.all().order_by('nome')
    return render(request, 'html/bancos.html', {'banco': banco})

def addBank(request):
    if request.method == 'POST':
        form = forms.AddBank(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/bank')
    else:
        form = forms.AddBank()
    return render(request, 'html/AddBanco.html', {'form': form})

def moviLogged(request):
    listMovi = models.Movimentos.objects.all()
    return render(request, 'html/movimento.html', {'movi': listMovi})

def addMoviment(request):
    if request.method == 'POST':
        form = forms.Movimento(request.POST)
        if form.is_valid():
            form.save(commit=False)
            tipo = form.cleaned_data['movimento']
            nome = form.cleaned_data['banco']
            valor = form.cleaned_data['valor']
            bancoSaldo = models.Banco.objects.all()
            nome = str(nome)
            tipo = str(tipo)
            for i in bancoSaldo:
                if i.nome == nome:
                    if tipo == 'E':
                        novoSaldo = i.saldo + valor
                    if tipo == 'S':
                        novoSaldo = i.saldo - valor
                    i.saldo = novoSaldo
                    i.save()
        return redirect('/home')
    else:
        form = forms.Movimento()
    return render(request, 'html/AddMovimento.html', {'form': form})

# def updateBank(request, nome):
#     banco = models.Banco.objects.all()
#     print(banco.saldo)
#     # if request.method == 'POST':
#     #     form = forms.AddBank(request.POST, instance = banco)
#     #     if form.is_valid():
#     #         form.save()
#     #     return redirect('/home')

#     return render (request, 'html/AddBanco.html')