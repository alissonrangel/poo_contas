from django.urls import path

app_name = 'gestor'

from . import views

urlpatterns = [
    path('adicionar-conta/', views.adicionar_conta, name='adicionar_conta'),
    path('contas-pagar/', views.lista_contas_pagar, name='lista_contas_pagar'),
    path('contas-receber/', views.lista_contas_receber, name='lista_contas_receber'),
    path('pessoas/', views.lista_adicionar_pessoa, name='lista_adicionar_pessoa'),
    path('editar-pessoa/<int:id_pessoa>/', views.editar_pessoa, name='editar_pessoa'),
    path('deletar-pessoa/<int:id_pessoa>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('criar-usuario/', views.add_user, name='add_user'),
    path('', views.home, name='home'), # a url vazia fica por ultimo
]