from django.urls import path
from .views import CadastroController, LoginController, PerfilController
from .views_contratacao import ContratacaoController
from .views_certificados import CertificadoController
from .views_anuncios import AnuncioController, Caretaker

contratacao_controller = ContratacaoController()
anuncio_controller = AnuncioController()
certificado_controller = CertificadoController()
cadastro_controller = CadastroController()
login_controller = LoginController()
perfil_controller = PerfilController()

urlpatterns = [
    #path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),

    path('anuncios/', anuncio_controller.getAnuncios, name='anuncios'),
    path('meus_anuncios/', anuncio_controller.getMeusAnuncios, name='meus_anuncios'),
    path('anuncio_edicao/<int:id>/', anuncio_controller.getMeuAnuncioById, name='anuncio_edicao'),
    path('anuncio_exclusao/<int:id>/', anuncio_controller.deleteAnuncio, name='anuncio_exclusao'),
    path('anuncio/<int:id>/', anuncio_controller.getAnuncioById, name='anuncio'),
    #path('perfil/<int:id>/', views.get_usuario_by_id, name='perfil')
    path('anuncio_editado/<int:anuncio_id>', anuncio_controller.updateAnuncio, name='anuncio_editado'),
    path('anuncio/criar/', anuncio_controller.createAnuncio, name='criar_anuncio'),
    path('anuncio/<int:anuncio_id>/versoes/', Caretaker.listarVersoesAnuncio, name='listar_versoes_anuncio'),
    path('anuncio/<int:anuncio_id>/restaurar/<int:snapshot_id>/', Caretaker.restaurarAnuncio, name='restaurar_anuncio'),

    path('certificados/', certificado_controller.get_certificados, name = "certificados"),
    path('adicionar_certificado/', certificado_controller.adicionar_certificado, name="adicionar_certificado"),

    path('perfil/<int:id>', perfil_controller.perfil, name="perfil"),
    path("login/", login_controller.login_simples, name='login'),
    path("logout/", login_controller.logout_simples, name='logout'),
    path('index/', login_controller.index, name='index'),
    path('', login_controller.index, name='index'),
    path('cadastro/', cadastro_controller.cadastro_usuario, name='cadastro'),


    path('anuncio/<int:id>/contratar/',  contratacao_controller.contratar, name='contratar'),
    path('contratacao/<int:id>/', contratacao_controller.get_contratacao_by_id, name='contratacao'),
    path('pendentes/', contratacao_controller.get_pendentes, name='pendentes'),
    path('pendente/<int:id>/', contratacao_controller.get_pendente_by_id, name='pendente'),
    path('historico/<int:finalizado>', contratacao_controller.get_contratacoes, name='historico'),
    path('contratacao/<int:contratacao_id>/aceitar/', contratacao_controller.aceitar_contratacao, name='aceitar_contratacao'),
    path('contratacao/<int:contratacao_id>/recusar/', contratacao_controller.recusar_contratacao, name='recusar_contratacao'),
    path('contratacao/<int:contratacao_id>/finalizar/', contratacao_controller.finalizar_contratacao, name='finalizar_contratacao'),
    path('contratar/<int:id>/', contratacao_controller.criar_contratacao, name='criar_contratacao'),
    


    #F2C438
]   