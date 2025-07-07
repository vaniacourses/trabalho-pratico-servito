from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import UsuarioForm, LoginForm
from datetime import date
from .services import DjangoStrategy, ApiStrategy
from django.conf import settings
from .models import Anuncio, Usuario
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

def get_anuncios(request):
    strategy = get_strategy()
    anuncios_list = strategy.get_list(Anuncio, None)
    paginator = Paginator(anuncios_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'anuncios.html', {'page_obj': page_obj})

def get_anuncio_by_id(request, id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, id)
    return render(request, 'anuncio_individual.html', {
        'anuncio': anuncio
        })

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
        
        #TODO usar o strategy aqui
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
        except usuario.DoesNotExist:
            error = "Credenciais inválidas."

    return render(request, "login.html", {"form": form, "error": error})






