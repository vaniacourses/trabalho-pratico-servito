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
from django.contrib.auth.hashers import make_password
from django.views import View
from django.contrib.auth.views import LogoutView
from .models import Anuncio, Adm, Usuario, Contratacao, Certificado
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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

def get_contratacoes(request, finalizado = 0):
    finalizado = bool(finalizado)
    strategy = get_strategy()
    email_logado = request.session.get('email')
    usuario = strategy.get_list(Usuario, {'email': email_logado})[0]
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
    contratacoes_list = usuario.historico(finalizado)
    if query:
        contratacoes_list = [a for a in contratacoes_list if query.lower() in a.titulo.lower() 
                         or query.lower() in a.descricao.lower() 
                         or query.lower() in a.tags.lower()]
    
    paginator = Paginator(contratacoes_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'historico.html', {
        'page_obj': page_obj,
        'query': query,  
        'usuario_logado': 'email' in request.session,
        'finalizado': int(finalizado)
    })

def get_contratacao_by_id(request, id):
    strategy = get_strategy()
    contratacao = strategy.get_single(Contratacao, id)
    return render(request, 'contratacao.html', {
        'contratacao': contratacao
        })

def aceitar_contratacao(request, contratacao_id):
    strategy = get_strategy()
    contratacao = strategy.get_single(Contratacao, contratacao_id)
    contratacao.pendente = False
    contratacao.aceito = True
    strategy.post(contratacao)
    return redirect('pendentes')

def recusar_contratacao(request, contratacao_id):
    strategy = get_strategy()
    contratacao = strategy.get_single(Contratacao, contratacao_id)
    contratacao.aceito = False
    contratacao.pendente = False
    strategy.post(contratacao)
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

        usuario = strategy.get_list(Usuario, {"email": email_logado})
        usuario = usuario[0] if usuario else None
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
        strategy.post(contratacao)
        messages.success(request, "Anúncio criado com sucesso!")
        return redirect('anuncios')
    return render(request, 'contratar.html', {'anuncio': anuncio})

def finalizar_contratacao(request, contratacao_id):
    strategy = get_strategy()
    contratacao = strategy.get_single(Contratacao, contratacao_id)

    email_logado = request.session.get('email')

    if not email_logado:
        messages.error(request, "Você precisa estar logado para finalizar uma contratação.")
        return redirect('login')

    
    if email_logado != contratacao.prestador.email:
        messages.error(request, "Você não tem permissão para finalizar esta contratação.")
        return redirect('contratacao', id=contratacao_id)

    if not contratacao.aceito:
        messages.error(request, "A contratação ainda não foi aceita.")
        return redirect('contratacao', id=contratacao_id)

    if contratacao.finalizado:
        messages.info(request, "Esta contratação já foi finalizada.")
        return redirect('contratacao', id=contratacao_id)

    contratacao.finalizado = True
    strategy.post(contratacao)

    messages.success(request, "Contratação finalizada com sucesso.")
    return redirect('contratacao', id=contratacao_id)