from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib
#from django.contrib.postgres.fields import ArrayField


class Cadastro(models.Model):
    nome = models.CharField(max_length=64, unique = True)
    email = models.CharField(max_length=64, unique = True)
    senha = models.CharField(max_length=64)
    telefone = models.CharField(max_length=64, unique=True)
    documento = models.CharField(max_length=64, unique=True)
    endereco = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    data_cadastro = models.DateField()
    class Meta:
        abstract = True


class Usuario(Cadastro):
    data_nascimento = models.DateField()
    is_banned = models.BooleanField(default = False)
    #related anuncios
    #related contratacoes

class Adm(Cadastro):
    cargo = models.CharField(max_length=64)


class Anuncio(models.Model):
    titulo = models.CharField(max_length=64, verbose_name="Título")
    descricao = models.CharField(max_length=1000, verbose_name="Descrição")
    #TODO deixar array com o pós postgree
    #tags = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    tags = models.CharField(max_length=640)
    cidade = models.CharField(max_length=64)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='anuncios')
    #related: contratacoes

class Contratacao(models.Model):
    preco = models.IntegerField(verbose_name="Preço", null=True)
    prazo = models.DateField(null=True)
    descricao = models.CharField(max_length=1000, verbose_name="Descrição")
    aceito = models.BooleanField(null=False)
    pendente = models.BooleanField(null=True)
    finalizado = models.BooleanField()
    #anuncio_origem = models.ManyToOneRel(Anuncio, on_delete=models.DO_NOTHING, related_name='anuncios')
    prestador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='prestador')
    contratante = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='contratante')



class Certificado(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    insituicao = models.CharField(max_length=100, verbose_name="Instituição")
    data = models.DateField()
    link = models.CharField(max_length=1000)
    pendente = models.BooleanField()
    aprovado = models.BooleanField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')