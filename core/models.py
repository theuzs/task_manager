from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    pass


class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    objetos = models.Manager()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Produto(models.Model):
    nome = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    objetos = models.Manager()

    def __str__(self):
        return f"{self.nome} [R$ {self.preco}]"


class Venda(models.Model):
    funcionario = models.ForeignKey(
        'Funcionario',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        'Produto',
        on_delete=models.CASCADE
    )

    data_hora = models.DateTimeField(
        auto_now_add=True
    )

    objetos = models.Manager()


# Novo modelo Atividade
class Atividade(models.Model):
    funcionario = models.ForeignKey(
        'Funcionario',
        on_delete=models.CASCADE,
        related_name="atividades"
    )

    titulo = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    descricao = models.TextField(
        null=True,
        blank=True
    )

    data = models.DateField(
        null=False,
        blank=False
    )

    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')],
        default='pendente'
    )

    objetos = models.Manager()

    def __str__(self):
        return f"{self.titulo} - {self.funcionario.nome}"
