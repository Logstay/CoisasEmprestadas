from django import forms
from .models import Coisa


class CoisasForm(forms.ModelForm):
    """ montando um form para melhorar no processo de validação """

    class Meta:
        # nome do banco
        model = Coisa
        # campos do modelo
        fields = [
            'item',
            'data_emprestimo',
            'data_devolucao',
            'contato_amigo',
            'usuario',
            'retorno'
        ]
