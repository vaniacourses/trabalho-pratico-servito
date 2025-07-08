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


class Caretaker:
    def atualizar_anuncio(request, anuncio_id):
        strategy = get_strategy()
        anuncio = strategy.get_single(Anuncio, anuncio_id)
        email_logado = request.session.get('email')
        if not email_logado or anuncio.usuario.email != email_logado:
            return redirect('meus_anuncios')

        if request.method == 'POST':
            # Antes de alterar, cria o backup (makeBackup)
            anuncio.criar_snapshot()

            anuncio.titulo = request.POST.get('titulo')
            anuncio.descricao = request.POST.get('descricao')
            anuncio.tags = request.POST.get('tags')
            anuncio.cidade = request.POST.get('cidade')
            strategy.post(anuncio)

            messages.success(request, "Anúncio atualizado e snapshot criado.")
            return redirect('meus_anuncios')

        return render(request, 'editar_anuncio.html', {'anuncio': anuncio})

    def restaurar_anuncio(request, anuncio_id, snapshot_id):
        strategy = get_strategy()
        anuncio = strategy.get_single(Anuncio, anuncio_id)
        snapshot = anuncio.snapshots.get(id=snapshot_id)
        email_logado = request.session.get('email')
        if not email_logado or anuncio.usuario.email != email_logado:
            return redirect('meus_anuncios')

        snapshot.restaurar()  # restaura o estado no anuncio
        messages.success(request, "Anúncio restaurado para versão anterior.")
        return redirect('meus_anuncios')
    
    def listar_versoes_anuncio(request, anuncio_id):
        strategy = get_strategy()
        anuncio = strategy.get_single(Anuncio, anuncio_id)

        email_logado = request.session.get('email')
        if not email_logado or anuncio.usuario.email != email_logado:
            return redirect('meus_anuncios')

        snapshots = anuncio.snapshots.all().order_by('-criado_em')
        return render(request, 'listar_snapshots.html', {
            'anuncio': anuncio,
            'snapshots': snapshots
        })


def get_strategy():
    return ApiStrategy() if settings.USE_API else DjangoStrategy()

def anuncios(request):
    strategy = get_strategy()
    if 'email' not in request.session:
        return redirect('login')
    email = request.session['email']
    usuario = strategy.get_list(Usuario, {'email':email})
    return render(request, 'anuncios.html', {'usuario_logado': request.user.is_authenticated})

def get_anuncios(request):
    strategy = get_strategy()
    query = request.GET.get('q', '')
    if query:
        anuncios_list = strategy.get_list(Anuncio, None)
        anuncios_list = [a for a in anuncios_list if query.lower() in a.titulo.lower() 
                         or query.lower() in a.descricao.lower() 
                         or query.lower() in a.tags.lower()]
    else:
        anuncios_list = strategy.get_list(Anuncio, None)
    paginator = Paginator(anuncios_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'anuncios.html', {
        'page_obj': page_obj,
        'query': query,  
        'usuario_logado': 'email' in request.session
    })

def get_meus_anuncios(request):
    strategy = get_strategy()
    email_logado = request.session.get('email')
    if not email_logado:
        return render(request, 'index.html')
    query = request.GET.get('q', '')
    filters={
        'usuario__email': email_logado
    }
    anuncios_list = strategy.get_list(Anuncio, filters)
    if query:
        anuncios_list = [a for a in anuncios_list if query.lower() in a.titulo.lower() 
                         or query.lower() in a.descricao.lower() 
                         or query.lower() in a.tags.lower()]
    paginator = Paginator(anuncios_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'meus_anuncios.html', {
        'page_obj': page_obj,
        'query': query,  
        'usuario_logado': 'email' in request.session
    })

def get_meu_anuncio_by_id(request, id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, id)
    return render(request, 'anuncio_edicao.html', {
        'anuncio': anuncio
        })

def get_anuncio_by_id(request, id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, id)
    return render(request, 'anuncio_individual.html', {
        'anuncio': anuncio
        })

def anuncio_edicao(request, anuncio_id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, anuncio_id)
    email_logado = request.session.get('email')
    if not email_logado or anuncio.usuario.email != email_logado:
        return redirect('meus_anuncios')
    

    if request.method == 'POST':

        anuncio.criar_snapshot()

        anuncio.titulo = request.POST.get('titulo')
        anuncio.tags = request.POST.get('tags')
        anuncio.cidade = request.POST.get('cidade')
        anuncio.descricao = request.POST.get('descricao')

        strategy.post(anuncio)

        messages.success(request, "Anúncio atualizado com sucesso!")

        return redirect('meus_anuncios')  

    return render(request, 'editar_anuncio.html', {'anuncio': anuncio})

def anuncio_exclusao(request, id):
    strategy = get_strategy()
    anuncio = strategy.get_single(Anuncio, id)
    email_logado = request.session.get('email')
    if not email_logado or email_logado != anuncio.usuario.email:
        return redirect('meus_anuncios')  

    if request.method == 'POST':
        strategy.delete(anuncio)
        return redirect('meus_anuncios')
    else:
        
        return redirect('meus_anuncios')


def criar_anuncio(request):
    strategy = get_strategy()
    email_logado = request.session.get('email')
    if not email_logado:
        return redirect('index')  

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        tags = request.POST.get('tags')
        cidade = request.POST.get('cidade')

        
        usuarios = strategy.get_list(Usuario, {"email": email_logado})
        usuario = usuarios.first() if usuarios else None
        if not usuario:
            messages.error(request, "Usuário não encontrado.")
            return redirect('index')

        
        anuncio = Anuncio(
            titulo=titulo,
            descricao=descricao,
            tags=tags,
            cidade=cidade,
            usuario=usuario
        )
        strategy.post(anuncio)
        messages.success(request, "Anúncio criado com sucesso!")
        return redirect('meus_anuncios')

    
    return render(request, 'criar_anuncio.html')