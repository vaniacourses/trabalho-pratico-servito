from django.urls import path
from .views import index, home, cadastro_usuario, anuncios,get_anuncios,get_anuncio_by_id,login_simples, logout_simples, teste_sessao, perfil, contratar, avaliar_contratacao, get_pendentes, get_contratacoes, get_contratacao_by_id, get_pendente_by_id, aceitar_contratacao, recusar_contratacao, get_meus_anuncios, get_meu_anuncio_by_id, anuncio_edicao, anuncio_exclusao, criar_anuncio, get_certificados, adicionar_certificado, criar_contratacao
urlpatterns = [
    #path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('cadastro/', cadastro_usuario, name='cadastro'),
    path('anuncios/', get_anuncios, name='anuncios'),
    path('meus_anuncios/', get_meus_anuncios, name='meus_anuncios'),
    path('anuncio_edicao/<int:id>/', get_meu_anuncio_by_id, name='anuncio_edicao'),
    path('anuncio_exclusao/<int:id>/', anuncio_exclusao, name='anuncio_exclusao'),
    path('anuncio/<int:id>/', get_anuncio_by_id, name='anuncio'),
    #path('perfil/<int:id>/', views.get_usuario_by_id, name='perfil')
    path('anuncio_editado/<int:anuncio_id>', anuncio_edicao, name='anuncio_editado'),
    path('anuncio/criar/', criar_anuncio, name='criar_anuncio'),
    path("login/", login_simples, name='login'),
    path("logout/", logout_simples, name='logout'),
    path('index/', index, name='index'),
    path('teste_sessao/', teste_sessao, name='teste_sessao'),
    path('anuncio/<int:id>/contratar/',  contratar, name='contratar'),
    path('contratacao/<int:id>/', get_contratacao_by_id, name='contratacao'),
    path('pendentes/', get_pendentes, name='pendentes'),
    path('pendente/<int:id>/', get_pendente_by_id, name='pendente'),
    path('historico/', get_contratacoes, name='historico'),
    path('contratacao/<int:contratacao_id>/aceitar/', aceitar_contratacao, name='aceitar_contratacao'),
    path('contratacao/<int:contratacao_id>/recusar/', recusar_contratacao, name='recusar_contratacao'),
    path('certificados/', get_certificados, name = "certificados"),
    path('adicionar_certificado/', adicionar_certificado, name="adicionar_certificado"),
    path('perfil/<int:id>', perfil, name="perfil"),
    path('contratar/<int:id>/', criar_contratacao, name='contratar')

    #F2C438
]   