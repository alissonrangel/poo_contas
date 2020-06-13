from django import forms

from .models import Conta, Pessoa

class ContaForm(forms.ModelForm):

    class Meta:
        model = Conta
        fields = '__all__' # ['pessoa','tipo_conta','vencimento','valor']

class PessoaForm(forms.ModelForm):
    
    class Meta:
        model = Pessoa
        fields = '__all__' # ['nome','nascimento','cpf']