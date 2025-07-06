from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import UsuarioForm
from datetime import date
from .services import DjangoStrategy, ApiStrategy
from django.conf import settings
from .models import Anuncio


def get_strategy():
    return ApiStrategy() if settings.USE_API else DjangoStrategy()

@login_required
def home(request):
    return render(request, "home.html")

def welcome(request):
    return render(request, "welcome.html")

def index(request):
    return render(request, "index.html")

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.data_cadastro = date.today()
            usuario.is_banned =  False
            strategy = get_strategy()
            strategy.post(form)
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

def get_anuncios(request):
    strategy = get_strategy()
    anuncios_list = strategy.get(Anuncio, None)
    paginator = Paginator(anuncios_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'anuncios.html', {'page_obj': page_obj})


class MeuLoginView(LoginView):
    template_name = 'login.html'

    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class MeuLogoutView(LogoutView):
    template_name = 'logout.html'

    success_url = reverse_lazy('welcome')

    def get_success_url(self):
        return self.success_url






