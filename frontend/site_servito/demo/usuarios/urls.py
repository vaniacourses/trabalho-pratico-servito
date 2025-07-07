from django.urls import path
from .views import index, home, cadastro_usuario, anuncios,get_anuncios,get_anuncio_by_id,login_simples, logout_simples, teste_sessao, contratar, avaliar_contratacao, get_pendentes, get_contratacoes, get_contratacao_by_id, get_pendente_by_id, aceitar_contratacao, recusar_contratacao
urlpatterns = [
    #path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('cadastro/', cadastro_usuario, name='cadastro'),
    path('anuncios/', get_anuncios, name='anuncios'),
    path('anuncio/<int:id>/', get_anuncio_by_id, name='anuncio'),
    #path('perfil/<int:id>/', views.get_usuario_by_id, name='perfil')

    path("login/", login_simples, name='login'),
    path("logout/", logout_simples, name='logout'),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('teste_sessao/', teste_sessao, name='teste_sessao'),
    path('anuncio/<int:id>/contratar/',  contratar, name='contratar'),
    path('contratacao/<int:id>/', get_contratacao_by_id, name='contratacao'),
    path('pendentes/', get_pendentes, name='pendentes'),
    path('pendente/<int:id>/', get_pendente_by_id, name='pendente'),
    path('historico/', get_contratacoes, name='historico'),
    path('contratacao/<int:contratacao_id>/aceitar/', aceitar_contratacao, name='aceitar_contratacao'),
    path('contratacao/<int:contratacao_id>/recusar/', recusar_contratacao, name='recusar_contratacao'),


    #F2C438
]