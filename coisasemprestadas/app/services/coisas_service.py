from ..models import Coisas_usr
from django.db import connection

''' metodo service que acessa diretamente o BD '''

# returna a lista de objetos cadastrados no BD
def listar_coisa():
    coisa = Coisas_usr.objects.all()
    return coisa

# retorna lista de objetos especificados por id
def listar_coisa_id(id):
    coisa = Coisas_usr.objects.get(id=id)
    return coisa

# remove diretamente o objeto do BD
def remover_coisa(coisa):
    coisa.delete()

# acessa o metodo create com os argumentos espeficos para criação do objeto no BD
def cadastrar_coisa(coisa):
    Coisas_usr.objects.create(
        item_usr=coisa.item_usr, 
        data_emprestimo_usr=coisa.data_emprestimo_usr, 
        data_devolucao_usr=coisa.data_devolucao_usr, 
        contato_amigo_usr=coisa.contato_amigo_usr,
        usuario=coisa.usuario
        )

# entra com o objeto já criado e com o 2 argumento substitui-o
def editar_coisa(coisa, nova_coisa):
    coisa.item_usr = nova_coisa.item_usr
    coisa.data_emprestimo_usr = nova_coisa.data_emprestimo_usr
    coisa.data_devolucao_usr = nova_coisa.data_devolucao_usr
    coisa.contato_amigo_usr = nova_coisa.contato_amigo_usr
    coisa.usuario = nova_coisa.usuario
    coisa.save(force_update=True)