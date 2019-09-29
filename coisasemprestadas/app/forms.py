from django import forms
from .models import Coisas_usr


class CoisasForm(forms.ModelForm):
    ''' montando um form para melhorar no processo do validação '''
    class Meta:
        # nome do banco
        model = Coisas_usr
        #campos do modelo
        fields = [
            'item_usr', 
            'data_emprestimo_usr', 
            ' data_devolucao_usr ', 
            'contato_amigo_usr', 
            'usuario'
            ]