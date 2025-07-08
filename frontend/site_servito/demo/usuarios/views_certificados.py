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

class CertificadoController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CertificadoController, cls).__new__(cls)
        return cls._instance

    def excluir_certificado(self,request, id):
        if request.method == "POST":
            strategy = get_strategy()
            certificado = strategy.get_single(Certificado, id)
            if certificado.usuario.id == request.session.get('id'):
                strategy.delete(certificado)
        return redirect('certificados')

    def get_pending_certificados(self, request):
        filters = {
            'pendente': True,
        }
        strategy = get_strategy()
        certificados = strategy.get_list(Certificado, filters)
        return render(request, 'certificados_pendentes.html', {'certificados': certificados, 'usuario_logado': 'email' in request.session})


    #TODO mudar o diagrama de classes
    def avaliar_certificado(self, request, certificado_id, aprovar):
        if request.method == 'POST':
            strategy = get_strategy()
            certificado = strategy.get_single(Certificado, certificado_id)
            certificado.pendente = False 
            certificado.aprovado = True if aprovar == 'aprovar' else False
            #TODO mudar o strategy aqui
            strategy.post(certificado)
        return redirect('certificados_pendentes')

    def adicionar_certificado(self, request):
        strategy = get_strategy()

        if request.method == 'POST':
            form = CertificadoForm(request.POST)
            if form.is_valid():
                certificado = form.save(commit=False)
                certificado.usuario_id = request.session['id']
                certificado.pendente = True
                certificado.aprovado = False
                strategy.post(certificado)
                return redirect('certificados', id=request.session['id'])
        else:
            form = CertificadoForm()

        return render(request, 'adicionar_certificado.html', {'form': form, 'usuario_logado': 'email' in request.session})

    def get_certificados(self, request):
        usuario_id = request.session.get('id')
        strategy = get_strategy()
        if not usuario_id:
            return redirect('login')  
        filter_1 = {
            'usuario_id': usuario_id
        }
        certificados = strategy.get_list(Certificado, filter_1)
        return render(request, 'certificados.html', {'certificados': certificados, 'usuario_logado': 'email' in request.session,})