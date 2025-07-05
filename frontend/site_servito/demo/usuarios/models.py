from django.db import models
#from django.contrib.postgres.fields import ArrayField

class Cadastro(models.Model):
    nome = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True, primary_key=True)
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
    is_banned = models.BooleanField()
    #related anuncios
    #related contratacoes

class Adm(Cadastro):
    cargo = models.CharField()

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
    #TODO Mudar nas classes o preço para int
    preco = models.IntegerField(verbose_name="Preço")
    #TODO Mudar nas classes o prazo para datetime
    prazo = models.DateField()
    #TODO mudar nas classes a descricao para string normal
    descricao = models.CharField(max_length=1000, verbose_name="Descrição")
    aceito = models.BooleanField()
    finalizado = models.BooleanField()
    prestador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestador')
    contratante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratante')