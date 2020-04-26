from ..models import Coisa

''' metodo service que acessa diretamente o BD '''


# returna a lista de objetos cadastrados no BD
def listar_coisas(usuario):
    return Coisa.objetos.filter(usuario=usuario).all()


# retorna lista de objetos especificados por id
def listar_coisas_id(id):
    return Coisa.objetos.get(id=id)


# remove diretamente o objeto do BD
def remover_coisas(coisas):
    coisas.delete()


# acessa o metodo create com os argumentos espeficos para criação do objeto no BD
def cadastrar_coisas(coisas):
    Coisa.objetos.create(
        item=coisas.item,
        data_emprestimo=coisas.data_emprestimo,
        data_devolucao=coisas.data_devolucao,
        contato_amigo=coisas.contato_amigo,
        usuario=coisas.usuario,
        retorno=coisas.retorno
    )


# entra com o objeto já criado e com o 2 argumento substitui-o
def editar_coisa(coisas, nova_coisas):
    coisas.item = nova_coisas.item
    coisas.data_emprestimo = nova_coisas.data_emprestimo
    coisas.data_devolucao = nova_coisas.data_devolucao
    coisas.contato_amigo = nova_coisas.contato_amigo
    coisas.retorno = nova_coisas.retorno
    coisas.usuario = nova_coisas.usuario
    coisas.save(force_update=True)
