from django.db import models
# chamado de autenticação builtin Django
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# class a ser usada no ORM que será criada no BancodeDados
class Coisa(models.Model):
    RETORNO_CHOICES = [
        ('Devolvido', 'Devolvido'),
        ('Pendente', 'Pendente'),
    ]

    class Meta:
        ordering = ('item',)
        verbose_name = 'coisa'
        verbose_name_plural = 'coisa'

    # Obj a ser emprestado
    item = models.CharField(
        null=False,
        max_length=100,
        blank=False,
    )
    # data em que o objeti será emprestado
    data_emprestimo = models.DateField(
        null=False,
        blank=False,
    )
    # data em que o emprestimo será devolvido
    data_devolucao = models.DateField(
        null=False,
        blank=False,
    )
    # numero de contado do amigo.
    contato_amigo = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    ''' chamada do registration para autenticação '''
    # registration ligado ao emprestimo tipo 1-N
    usuario = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
    )

    retorno = models.CharField(
        max_length=10,
        choices=RETORNO_CHOICES,
        null=False,
        blank=False)

    def __str__(self):
        return self.item

    objetos = models.Manager()