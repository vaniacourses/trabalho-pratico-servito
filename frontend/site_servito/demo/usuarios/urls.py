from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.MeuLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro')
    #F2C438
]