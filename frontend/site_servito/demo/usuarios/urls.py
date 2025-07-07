from django.urls import path
from .views import login_simples
from .views import index, home, cadastro_usuario, anuncios


urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('anuncios/', views.get_anuncios, name='anuncios'),
    path('anuncio/<int:id>/', views.get_anuncio_by_id, name='anuncio'),
    #path('perfil/<int:id>/', views.get_usuario_by_id, name='perfil')

    path("login/", login_simples, name='login'),
    path('', index, name='index'),
    path('index/', home, name='index')
    #F2C438
]