from django import forms
from .models import Usuario, Adm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'email',
            'senha',
            'telefone',
            'documento',
            'endereco',
            'cidade',
            'data_nascimento',
        ]
        widgets = {
            'senha': forms.PasswordInput(),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "Seu email"}))
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={"placeholder": "Sua senha"}))
