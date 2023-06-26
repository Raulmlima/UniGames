from django.shortcuts import render, redirect
from .models import CPerfil
from django.contrib import messages


def home(request):
    return render(request, 'pages/home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        perfil = CPerfil.objects.filter(email=email, senha=senha).first()
        if perfil:
            return redirect('home')  # Redireciona para a página inicial
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
            new_perfil = CPerfil(email=email, senha=senha, nascimento=data_nascimento)
            new_perfil.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, 'As senhas não coincidem.')
    return render(request, 'login/login.html')

def saldo(request):
    return render(request, 'pages/saldo.html')

def perfil(request):
    return render(request, 'pages/perfil.html')



from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def request_withdrawal(request):
    if request.method == 'POST':
        withdrawal_amount = request.POST.get('withdrawal-amount')
        selected_method = request.POST.get('opcao')

        email_content = f"Valor do Saque: {withdrawal_amount}\n"
        email_content += f"Método de Saque: {selected_method}"

        send_mail(
            'Solicitação de Saque',
            email_content,
            settings.EMAIL_HOST_USER,
            ['hummy.solicitacoes@gmail.com'], 
            fail_silently=False,
        )

    return render(request, 'sua_template.html')

