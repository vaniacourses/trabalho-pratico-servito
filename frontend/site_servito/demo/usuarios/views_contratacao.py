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

def contratar(request, id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, id)

    return render(request, "contratar.html", {"anuncio": anuncio})

def avaliar_contratacao(request):
    return redirect('contratacao')

def get_pendentes(request):
    strategy = get_strategy()
    email_logado = request.session.get('email')
    if not email_logado:
        return render(request, 'index.html')
    filters = {
        'pendente': True,
        'prestador__email': email_logado
    }
    query = request.GET.get('q', '')
    pendentes_list = strategy.get_list(Contratacao, filters)
    if query:
        pendentes_list = [a for a in pendentes_list if query.lower() in a.titulo.lower() 
                         or query.lower() in a.descricao.lower() 
                         or query.lower() in a.tags.lower()]
    paginator = Paginator(pendentes_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pendentes.html', {
        'page_obj': page_obj,
        'query': query,  
        'usuario_logado': 'email' in request.session
    })

def get_pendente_by_id(request, id):
    strategy = get_strategy()
    pendente = strategy.get_single(Contratacao, id)
    return render(request, 'pendente.html', {
        'pendente': pendente
        })

def get_contratacoes(request):
    strategy = get_strategy()
    email_logado = request.session.get('email')
    if not email_logado:
        return render(request, 'index.html')
    filters_1 = {
        'aceito': True,
        'contratante__email': email_logado
    }
    filters_2 = {
        'aceito': True,
        'prestador__email': email_logado
    }
    query = request.GET.get('q', '')
    contratacoes_list_1 = strategy.get_list(Contratacao, filters_1)
    contratacoes_list_2 = strategy.get_list(Contratacao, filters_2)
    contratacoes_list = list(set(contratacoes_list_1) | set(contratacoes_list_2))
    if query:
        contratacoes_list = [a for a in pendentes_list if query.lower() in a.titulo.lower() 
                         or query.lower() in a.descricao.lower() 
                         or query.lower() in a.tags.lower()]
    
    paginator = Paginator(contratacoes_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'historico.html', {
        'page_obj': page_obj,
        'query': query,  
        'usuario_logado': 'email' in request.session
    })

def get_contratacao_by_id(request, id):
    strategy = get_strategy()
    contratacao = strategy.get_single(Contratacao, id)
    return render(request, 'contratacao.html', {
        'contratacao': contratacao
        })

def aceitar_contratacao(request, contratacao_id):
    contratacao = get_object_or_404(Contratacao, id=contratacao_id)
    contratacao.pendente = False
    contratacao.aceito = True
    contratacao.save()
    return redirect('pendentes')

def recusar_contratacao(request, contratacao_id):
    contratacao = get_object_or_404(Contratacao, id=contratacao_id)
    contratacao.pendente = False
    contratacao.aceito = False
    contratacao.save()
    return redirect('pendentes')

def criar_contratacao(request, id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, id)
    prestador = anuncio.usuario
    email_logado = request.session.get('email')
    if not email_logado:
        return redirect('index')  

    if request.method == 'POST':
        prazo = request.POST.get('data')
        descricao = request.POST.get('detalhes')
        preco = request.POST.get('valor')

        usuario = Usuario.objects.filter(email=email_logado).first()
        if not usuario:
            messages.error(request, "Usuário não encontrado.")
            return redirect('index')
        contratacao = Contratacao(
                preco=preco,
                descricao=descricao,
                prazo=prazo,
                aceito=False,
                pendente=True,
                finalizado=False,
                contratante=usuario,
                prestador=prestador
            )
        contratacao.save()
        messages.success(request, "Anúncio criado com sucesso!")
        return redirect('anuncios')
    return render(request, 'contratar.html', {'anuncio': anuncio})