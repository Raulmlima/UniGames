from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import CPerfil
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'pages/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        perfil = CPerfil.objects.filter(email=email, senha=senha).first()
        if perfil:
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    return render(request, 'login/login.html')

def leagueOfLegends(request):
    return render(request, 'pages/leagueOfLegends.html')

def valorant(request):
    return render(request, 'pages/Valorant.html')

def criarTorneio(request):
    return render(request, 'pages/criarTorneio.html')

def meusTorneios(request):
    return render(request, 'pages/meusTorneios.html')

def criarperfil(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        data_nascimento = request.POST.get('data_nascimento')

        if senha == confirmar_senha:
            if CPerfil.objects.filter(email=email).exists():
                messages.error(request, 'O email já está em uso.')
            else:
                new_perfil = CPerfil(email=email, senha=senha, nascimento=data_nascimento)
                new_perfil.save()
                messages.success(request, 'Conta criada com sucesso!')
                return redirect('login')
        else:
            messages.error(request, 'As senhas não coincidem.')
    
    return render(request, 'login/login.html')

def autenticar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    
    return render(request, 'login.html')

def saldo(request):
    return render(request, 'pages/saldo/saldo.html')

def perfil(request):
    return render(request, 'pages/perfil.html')