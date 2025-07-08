from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib
#from django.contrib.postgres.fields import ArrayField


class Cadastro(models.Model):
    nome = models.CharField(max_length=64)
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

    def historico(self, finalizado = True):
        como_contratante = set(self.contratante.filter(finalizado=finalizado))
        como_prestador = set(self.prestador.filter(finalizado=finalizado))
        return list(como_contratante | como_prestador)


class Adm(Cadastro):
    cargo = models.CharField(max_length=64)

class AnuncioSnapshot(models.Model):
    anuncio = models.ForeignKey('Anuncio', on_delete=models.CASCADE, related_name='snapshots')
    titulo = models.CharField(max_length=64)
    descricao = models.CharField(max_length=1000)
    tags = models.CharField(max_length=640)
    cidade = models.CharField(max_length=64)
    criado_em = models.DateTimeField(auto_now_add=True)
    def restaurar(self):
        
        self.anuncio.restaurar_snapshot(self)

    def __str__(self):
        return f"Snapshot de {self.anuncio.titulo} em {self.criado_em}"



class Anuncio(models.Model):
    titulo = models.CharField(max_length=64, verbose_name="Título")
    descricao = models.CharField(max_length=1000, verbose_name="Descrição")
    tags = models.CharField(max_length=640)
    cidade = models.CharField(max_length=64)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='anuncios')
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def criar_snapshot(self):
        return AnuncioSnapshot.objects.create(
            anuncio=self,
            titulo=self.titulo,
            descricao=self.descricao,
            tags=self.tags,
            cidade=self.cidade
        )
    
    def restaurar_snapshot(self, snapshot: 'AnuncioSnapshot'):
        
        if snapshot.anuncio != self:
            raise ValueError("Snapshot não pertence a este anúncio.")
        self.titulo = snapshot.titulo
        self.descricao = snapshot.descricao
        self.tags = snapshot.tags
        self.cidade = snapshot.cidade
        self.save()

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
    instituicao = models.CharField(max_length=100, verbose_name="Instituição")
    data = models.DateField()
    link = models.CharField(max_length=1000)
    pendente = models.BooleanField()
    aprovado = models.BooleanField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')