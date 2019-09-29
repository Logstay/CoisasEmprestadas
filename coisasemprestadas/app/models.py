from django.db import models
# chamado de autenticação builtin Django
from django.contrib.auth.models import User

# class a ser usada no ORM que será criada no BancodeDados
class Coisas_usr(models.Model):

    #Obj a ser emprestado
    item_usr = models.CharField(
        null=False,
        max_length=100,
        blank=False,
        )
    #data em que o objeti será emprestado
    data_emprestimo_usr = models.DateField(
        null=False,
        blank=False,
    )
    #data em que o emprestimo será devolvido
    data_devolucao_usr = models.DateField(
         null=False,
        blank=False,
    )
    # numero de contado do amigo.
    contato_amigo_usr = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    ''' chamada do usuario para autenticação '''
    # usuario ligado ao emprestimo tipo 1-N
    usuario = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
    )

    objetos = models.Manager()

