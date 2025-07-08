from django.urls import path
from .views import UsuarioController, LoginController, PerfilController
from .views_contratacao import ContratacaoController
from .views_certificados import CertificadoController
from .views_anuncios import AnuncioController, Caretaker

contratacao_controller = ContratacaoController()
anuncio_controller = AnuncioController()
certificado_controller = CertificadoController()
usuario_controller = UsuarioController()
login_controller = LoginController()
perfil_controller = PerfilController()
caretaker = Caretaker()

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
    path('anuncio/<int:anuncio_id>/versoes/', caretaker.listarVersoesAnuncio, name='listar_versoes_anuncio'),
    path('anuncio/<int:anuncio_id>/restaurar/<int:snapshot_id>/', caretaker.restaurarAnuncio, name='restaurar_anuncio'),

    path('certificados/', certificado_controller.getCertificados, name = "certificados"),
    path('adicionar_certificado/', certificado_controller.createCertificado, name="adicionar_certificado"),

    path('perfil/<int:id>', perfil_controller.perfil, name="perfil"),
    path("login/", login_controller.loginSimples, name='login'),
    path("logout/", login_controller.logoutSimples, name='logout'),
    path('index/', login_controller.index, name='index'),
    path('', login_controller.index, name='index'),
    path('cadastro/', usuario_controller.createUsuario, name='cadastro'),


    path('anuncio/<int:id>/contratar/',  contratacao_controller.contratar, name='contratar'),
    path('contratacao/<int:id>/', contratacao_controller.getContratacaoById, name='contratacao'),
    path('pendentes/', contratacao_controller.getPendentes, name='pendentes'),
    path('pendente/<int:id>/', contratacao_controller.getPendenteById, name='pendente'),
    path('historico/<int:finalizado>', contratacao_controller.getContratacoes, name='historico'),
    path('contratacao/<int:contratacao_id>/aceitar/', contratacao_controller.aceitarContratacao, name='aceitar_contratacao'),
    path('contratacao/<int:contratacao_id>/recusar/', contratacao_controller.recusarContratacao, name='recusar_contratacao'),
    path('contratacao/<int:contratacao_id>/finalizar/', contratacao_controller.finalizarContratacao, name='finalizar_contratacao'),
    path('contratar/<int:id>/', contratacao_controller.createContratacao, name='criar_contratacao'),
    


    #F2C438
]   