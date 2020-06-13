from django import forms
from django.contrib.auth.models import User

from .models import Conta, Pessoa

class ContaForm(forms.ModelForm):

    class Meta:
        model = Conta
        fields = '__all__' # ['pessoa','tipo_conta','vencimento','valor']

class PessoaForm(forms.ModelForm):
    
    class Meta:
        model = Pessoa
        fields = '__all__' # ['nome','nascimento','cpf']

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password'] # 'email'