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
from .models import Adm, Usuario, Contratacao
from django.contrib import messages



def get_strategy():
    return ApiStrategy() if settings.USE_API else DjangoStrategy()

@login_required
def home(request):
    return render(request, "home.html")

def welcome(request):
    return render(request, "welcome.html")

def index(request):
    if 'email' in request.session:
        return render(request, 'index.html', {'usuario_logado': True})
    else:
        return render(request, 'index.html', {'usuario_logado': False})

def anuncios(request):
    if 'email' not in request.session:
        return redirect('login')
    email = request.session['email']
    usuario = Usuario.objects.get(email=email)
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
    usuario = None
    form = LoginForm(request.POST or None)
    error = None

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        senha = form.cleaned_data["senha"]
        
        #TODO usar o strategy aqui
        # Verifica se é adm
        try:
            adm = Adm.objects.get(email=email, senha=senha)
            request.session['email'] = adm.email
            return redirect("/certificados/")
        except Adm.DoesNotExist:    
            pass

        # Verifica se é usuario
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            request.session['email'] = usuario.email
            return redirect("/anuncios/")
        except Usuario.DoesNotExist:
            error = "Credenciais inválidas."

    return render(request, "login.html", {"form": form, "error": error})

def logout_simples(request):
    request.session.flush()
    return redirect('index')  

def teste_sessao(request):
    if 'visitas' in request.session:
        request.session['visitas'] += 1
    else:
        request.session['visitas'] = 1
    return HttpResponse(f"Visitas: {request.session['visitas']}")

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

def anuncio_edicao(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    if request.user != anuncio.usuario:
        return redirect('meus_anuncios')

    if request.method == 'POST':
        
        titulo = request.POST.get('titulo')
        tags = request.POST.get('tags')
        cidade = request.POST.get('cidade')
        descricao = request.POST.get('descricao')

        
        anuncio.titulo = titulo
        anuncio.tags = tags
        anuncio.cidade = cidade
        anuncio.descricao = descricao
        anuncio.save()

        return redirect('meus_anuncios')  

    return render(request, 'editar_anuncio.html', {'anuncio': anuncio})

def anuncio_exclusao(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    email_logado = request.session.get('email')
    if not email_logado or email_logado != anuncio.usuario.email:
        return redirect('meus_anuncios')  

    if request.method == 'POST':
        anuncio.delete()
        return redirect('meus_anuncios')
    else:
        
        return redirect('meus_anuncios')


def criar_anuncio(request):
    email_logado = request.session.get('email')
    if not email_logado:
        return redirect('index')  

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        tags = request.POST.get('tags')
        cidade = request.POST.get('cidade')

        
        usuario = Usuario.objects.filter(email=email_logado).first()
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
        anuncio.save()
        messages.success(request, "Anúncio criado com sucesso!")
        return redirect('meus_anuncios')

    
    return render(request, 'criar_anuncio.html')








