from django.contrib import admin

from .models import Pessoa, Conta

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Conta)

