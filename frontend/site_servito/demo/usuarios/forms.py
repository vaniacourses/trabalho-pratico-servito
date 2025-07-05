from django import forms
from .models import Usuario

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