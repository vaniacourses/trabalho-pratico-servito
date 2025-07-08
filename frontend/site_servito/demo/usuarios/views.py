from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import UsuarioForm, LoginForm, CertificadoForm
from datetime import date
from .services import DjangoStrategy, ApiStrategy
from django.conf import settings
from .models import Anuncio, Usuario
from django.contrib.auth.hashers import make_password
from django.views import View
from django.contrib.auth.views import LogoutView
from .models import Adm, Usuario, Contratacao, Certificado
from django.contrib import messages



def get_strategy():
    return ApiStrategy() if settings.USE_API else DjangoStrategy()

def index(request):
    if 'email' in request.session:
        return render(request, 'index.html', {'usuario_logado': True})
    else:
        return render(request, 'index.html', {'usuario_logado': False})


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
            strategy.post(usuario)
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})


# def get_user_by_id(request, id):
#     strategy = get_strategy()
#     usuario = strategy.get_single(usuario, id)

#     if request.method == 'POST':
#         form = UsuarioUpdateForm(request.POST, instance=usuario_obj)
#         if form.is_valid():
#             form.save()
#             return redirect('perfil')  # ou alguma mensagem de sucesso
#     else:
#         form = UsuarioUpdateForm(instance=usuario_obj)

#     return render(request, 'usuarios/perfil.html', {'form': form})

#     return render(request, 'perfil.html', {
#         'usuario': Usuario
#         })


'''
class MeuLoginView(LoginView):
    template_name = 'login.html'

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            #TODO usar o strategy aqui
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                form.add_error(None, 'E-mail ou senha inválidos.')

        return render(request, 'login.html', {'form': form})
'''
'''
class MeuLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index') 
'''

def login_simples(request):
    strategy = get_strategy()
    usuario = None
    form = LoginForm(request.POST or None)
    error = None

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        senha = form.cleaned_data["senha"]

        # Verifica se é adm
        adm = strategy.get_list(Adm, {"email": email, "senha": senha}).first()
        if adm is not None:
            request.session['email'] = adm.email
            request.session['id'] = adm.id
            return redirect("/certificadosPendentes/")

        # Verifica se é usuario
        usuario = strategy.get_list(Usuario, {"email": email, "senha": senha}).first()
        if usuario is not None:
            request.session['email'] = usuario.email
            request.session['id'] = usuario.id
            return redirect("/index/")

        # Se nenhum dos dois achou
        error = "Credenciais inválidas."

    return render(request, "login.html", {"form": form, "error": error})


def logout_simples(request):
    request.session.flush()
    return redirect('index')  

def perfil(request, id):
    strategy = get_strategy()
    usuario = strategy.get_single(Usuario, id)

    #TODO usar strategy aqui
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            strategy.post(form)
            return redirect('perfil', id=usuario.id)  # redireciona para o próprio perfil
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'perfil.html', {'form': form})