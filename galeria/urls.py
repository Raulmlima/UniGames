from django.urls import path
from .views import home, login, criarperfil, leagueOfLegends, valorant, criarTorneio, meusTorneios, saldo, perfil

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('leagueOfLegends/', leagueOfLegends, name='leagueOfLegends'),
    path('valorant/', valorant, name='valorant'),
    path('criarTorneio/', criarTorneio, name='criarTorneio'),
    path('meusTorneios/', meusTorneios, name='meusTorneios'),
    path('perfil/', perfil, name='perfil'),
    path('saldo/', saldo, name='saldo'),
    path('criarperfil/', criarperfil, name='criarperfil'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('request_withdrawal/', views.request_withdrawal, name='request_withdrawal'),
]
