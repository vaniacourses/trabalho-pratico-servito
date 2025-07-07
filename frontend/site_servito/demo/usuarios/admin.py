from django.contrib import admin
from .models import Usuario, Adm, Anuncio, Contratacao, Certificado
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Adm)
admin.site.register(Anuncio)
admin.site.register(Contratacao)
admin.site.register(Certificado)
