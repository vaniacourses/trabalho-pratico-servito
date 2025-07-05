from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse



@login_required
def home(request):
    return render(request, "home.html")

def welcome(request):
    return render(request, "welcome.html")

def index(request):
    return render(request, "index.html")

def cadastro(request):
    return render(request, "cadastro.html")

class MeuLoginView(LoginView):
    template_name = 'login.html'

    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class MeuLogoutView(LogoutView):
    template_name = 'logout.html'

    success_url = reverse_lazy('welcome')

    def get_success_url(self):
        return self.success_url






