from django.urls import path
from .views import login_simples
from .views import index, home, cadastro_usuario, anuncios


urlpatterns = [
    path("login/", login_simples, name='login'),
    path('', index, name='index'),
    path('index/', home, name='index'),
    path('cadastro/', cadastro_usuario, name='cadastro'),
    path('anuncios/', anuncios, name='anuncios')
    #F2C438
]