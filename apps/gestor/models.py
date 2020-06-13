from django.db import models
from django.db.models import Sum

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=200)
    nascimento = models.DateField(verbose_name='Nascimento')
    cpf = models.CharField(verbose_name='CPF', max_length=14)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    TIPO_CONTA_CHOICE = (
        ('RB', 'A Receber'),
        ('PG', 'A Pagar')
    )
    pessoa = models.ForeignKey(Pessoa, verbose_name="Pessoa", on_delete=models.CASCADE)
    tipo_conta = models.CharField(verbose_name="Tipo de conta", max_length=2, choices=TIPO_CONTA_CHOICE)
    vencimento = models.DateField(verbose_name="Vencimento")
    valor = models.DecimalField(verbose_name="Valor R$", max_digits=19, decimal_places=2)

    def __str__(self):
        return "Nome: {} - Valor: {}".format(self.pessoa.nome, self.valor)

    '''
    def get_total_contas_pagar(self):
        model = self.__class__ # Conta.objects.all()
        total = model.objects.filter(tipo_conta='PG').aggregate(Sum('valor'))
        return total
    '''