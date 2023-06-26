from django.urls import path
from .views import home, login_view, criarperfil, leagueOfLegends, valorant, criarTorneio, meusTorneios, saldo, perfil, autenticar

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('leagueOfLegends/', leagueOfLegends, name='leagueOfLegends'),
    path('valorant/', valorant, name='valorant'),
    path('criarTorneio/', criarTorneio, name='criarTorneio'),
    path('meusTorneios/', meusTorneios, name='meusTorneios'),
    path('perfil/', perfil, name='perfil'),
    path('saldo/', saldo, name='saldo'),
    path('criarperfil/', criarperfil, name='criarperfil'),
    path('autenticar/', autenticar, name='autenticar'),
]