from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Conta, Pessoa
from .forms import ContaForm, PessoaForm, UserForm
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gestor:home')
        else:
            messages.error(request, 'Usuário ou senha inválido.')
    return render(request, 'user_login.html', {})

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('gestor:user_login')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            return redirect('gestor:user_login')
    form = UserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required(login_url='/login/')
def home(request):
    lista_contas = Conta.objects.all()  # QuerySet
    return render(request, 'base.html', {'lista_contas' : lista_contas})

@login_required(login_url='/login/')
def adicionar_conta(request):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor:home')
    form = ContaForm()
    return render(request, 'adicionar_conta.html', {'form': form})

@login_required(login_url='/login/')
def lista_contas_pagar(request):
    contas_pagar = Conta.objects.filter(tipo_conta='PG')
    total = contas_pagar.aggregate(Sum('valor'))['valor__sum']
    return render(request, 'lista_contas_pagar.html', {'contas_pagar':contas_pagar, 'total': total})

@login_required(login_url='/login/')
def lista_contas_receber(request):
    contas_receber = Conta.objects.filter(tipo_conta='RB')
    total = contas_receber.aggregate(Sum('valor'))['valor__sum']
    return render(request, 'lista_contas_receber.html', {'contas_receber':contas_receber, 'total': total})

@login_required(login_url='/login/')
def lista_adicionar_pessoa(request):
    pessoas = Pessoa.objects.all()
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor:lista_adicionar_pessoa')
    form = PessoaForm()
    return render(request, 'lista_adicionar_pessoa.html', {'form': form, 'pessoas': pessoas})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def deletar_pessoa(request, id_pessoa):
    Pessoa.objects.get(id=id_pessoa).delete()
    return redirect('gestor:lista_adicionar_pessoa')