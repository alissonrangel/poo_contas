from django.shortcuts import render, redirect
from django.db.models import Sum

from .models import Conta, Pessoa
from .forms import ContaForm, PessoaForm
# Create your views here.

def home(request):
    lista_contas = Conta.objects.all()  # QuerySet
    return render(request, 'base.html', {'lista_contas' : lista_contas})

def adicionar_conta(request):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor:home')
    form = ContaForm()
    return render(request, 'adicionar_conta.html', {'form': form})

def lista_contas_pagar(request):
    contas_pagar = Conta.objects.filter(tipo_conta='PG')
    total = contas_pagar.aggregate(Sum('valor'))['valor__sum']
    return render(request, 'lista_contas_pagar.html', {'contas_pagar':contas_pagar, 'total': total})

def lista_contas_receber(request):
    contas_receber = Conta.objects.filter(tipo_conta='RB')
    total = contas_receber.aggregate(Sum('valor'))['valor__sum']
    return render(request, 'lista_contas_receber.html', {'contas_receber':contas_receber, 'total': total})

def lista_adicionar_pessoa(request):
    pessoas = Pessoa.objects.all()
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor:lista_adicionar_pessoa')
    form = PessoaForm()
    return render(request, 'lista_adicionar_pessoa.html', {'form': form, 'pessoas': pessoas})

def editar_pessoa(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    pessoas = Pessoa.objects.all()
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('gestor:lista_adicionar_pessoa')
    form = PessoaForm(instance=pessoa)
    return render(request, 'lista_adicionar_pessoa.html', {'form': form, 'pessoas': pessoas})