class Coisas_usr():
    def __init__(self,item_usr, data_emprestimo_usr, data_devolucao_usr, contato_amigo_usr, usuario):
        self.__item_usr = item_usr
        self.__data_emprestimo_usr = data_emprestimo_usr
        self.__data_devolucao_usr = data_devolucao_usr
        self.__contato_amigo_usr = contato_amigo_usr
        self.__usuario = usuario

       

    @property
    def item_usr(self):
        return self.__item_usr

    @item_usr.setter
    def item_usr(self, item_usr):
        self.__item_usr = item_usr

    @property
    def data_emprestimo_usr(self):
        return self.__data_emprestimo_usr

    @data_emprestimo_usr.setter
    def data_emprestimo_usr(self, data_emprestimo_usr):
        self.__data_emprestimo_usr = data_emprestimo_usr

    @property
    def data_devolucao_usr(self):
        return self.__data_devolucao_usr

    @data_devolucao_usr.setter
    def data_devolucao_usr(self, data_devolucao_usr):
        self.__data_devolucao_usr = data_devolucao_usr

    @property
    def contato_amigo_usr(self):
        return self.__contato_amigo_usr

    @contato_amigo_usr.setter
    def contato_amigo_usr(self, contato_amigo_usr):
        self.__contato_amigo_usr = contato_amigo_usr

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario