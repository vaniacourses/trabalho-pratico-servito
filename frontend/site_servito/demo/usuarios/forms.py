from django import forms
from .models import Usuario, Adm, Certificado

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
            'senha': forms.PasswordInput(render_value=True),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        exclude = ['pendente', 'aprovado', 'usuario']  # Serão definidos automaticamente
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input-field'}),
            'titulo': forms.TextInput(attrs={'class': 'input-field'}),
            'insituicao': forms.TextInput(attrs={'class': 'input-field'}),
            'link': forms.URLInput(attrs={'class': 'input-field'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "Seu email"}))
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={"placeholder": "Sua senha"}))
