from django.urls import path
from . import views
urlpatterns = [
    #path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('anuncios/', views.get_anuncios, name='anuncios'),
    path('anuncio/<int:id>/', views.get_anuncio_by_id, name='anuncio'),
    #path('perfil/<int:id>/', views.get_usuario_by_id, name='perfil')

    path("login/", views.login_simples, name='login'),
    path("logout/", views.logout_simples, name='logout'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('teste_sessao/', views.teste_sessao, name='teste_sessao'),
    path('anuncio/<int:id>/contratar/',  views.contratar, name='contratar'),
    path('contratacao/<int:id>/', views.get_contratacao_by_id, name='contratacao'),
    path('pendentes/', views.get_pendentes, name='pendentes'),
    path('pendente/<int:id>/', views.get_pendente_by_id, name='pendente'),
    path('historico/', views.get_contratacoes, name='historico'),
    path('contratacao/<int:contratacao_id>/aceitar/', views.aceitar_contratacao, name='aceitar_contratacao'),
    path('contratacao/<int:contratacao_id>/recusar/', views.recusar_contratacao, name='recusar_contratacao'),
    path('certificadosPendentes/', views.get_pending_certificados, name='certificados_pendentes'),
    path('certificadosPendentes/avaliar/<int:certificado_id>/<str:aprovar>/', views.avaliar_certificado, name='avaliar_certificado'),
    path('perfil/<int:id>/', views.perfil, name='perfil'),
    path('certificados/', views.get_certificados, name='certificados'),
    path('certificados/adicionar/', views.adicionar_certificado, name='adicionar_certificado'),
    path('certificados/excluir/<int:id>/', views.excluir_certificado, name='excluir_certificado'),







    #F2C438
]