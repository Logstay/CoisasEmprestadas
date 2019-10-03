class Coisa:
    def __init__(self, item, data_emprestimo, data_devolucao, contato_amigo, usuario, retorno):
        self._item = item
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = data_devolucao
        self._contato_amigo = contato_amigo
        self._usuario = usuario
        self.retorno = retorno

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    @data_emprestimo.setter
    def data_emprestimo(self, data_emprestimo):
        self._data_emprestimo = data_emprestimo

    @property
    def data_devolucao(self):
        return self._data_devolucao

    @data_devolucao.setter
    def data_devolucao(self, data_devolucao):
        self._data_devolucao = data_devolucao

    @property
    def contato_amigo(self):
        return self._contato_amigo

    @contato_amigo.setter
    def contato_amigo(self, contato_amigo):
        self._contato_amigo = contato_amigo

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def retorno(self):
        return self._retorno

    @retorno.setter
    def retorno(self, retorno):
        self._retorno = retorno
