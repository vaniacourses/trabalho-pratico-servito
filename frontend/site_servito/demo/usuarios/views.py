from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import UsuarioForm, LoginForm
from datetime import date
from .services import DjangoStrategy, ApiStrategy
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.views import View
from django.contrib.auth.views import LogoutView
from .models import Adm, Usuario


def get_strategy():
    return ApiStrategy() if settings.USE_API else DjangoStrategy()

@login_required
def home(request):
    return render(request, "home.html")

def welcome(request):
    return render(request, "welcome.html")

def index(request):
    return render(request, 'index.html', {'usuario_logado': request.user.is_authenticated})

def anuncios(request):
    return render(request, 'anuncios.html', {'usuario_logado': request.user.is_authenticated})


def cadastro(request):
    return render(request, "cadastro.html")

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.data_cadastro = date.today()
            usuario.is_banned =  False
            usuario.senha = form.cleaned_data['senha']
            strategy = get_strategy()
            strategy.post(form)
            usuario.save()
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

'''
class MeuLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                form.add_error(None, 'E-mail ou senha inválidos.')

        return render(request, 'login.html', {'form': form})


class MeuLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index') 
'''

def login_simples(request):
    form = LoginForm(request.POST or None)
    error = None

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        senha = form.cleaned_data["senha"]

        # Verifica se é adm
        try:
            adm = Adm.objects.get(email=email, senha=senha)
            return redirect("/certificados/")
        except Adm.DoesNotExist:    
            pass

        # Verifica se é usuario
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            return redirect("/anuncios/")
        except Usuario.DoesNotExist:
            error = "Credenciais inválidas."

    return render(request, "login.html", {"form": form, "error": error})






