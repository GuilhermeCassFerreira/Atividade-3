class Cliente:

    def __init__(self,nome: str, fone: int, email: str):
            self.__nome = nome
            self.__fone = fone
            self.__email = email


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome: str):
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self,fone: int):
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email: str):
        self.__email = email
    

    """Insira aqui os demais metodos ... """

class PacoteViagem:

    def __init__(self, origem: str, destino: str, duracao: int, custo_unitario: int):
        self.__origem = origem
        self.__destino = destino
        self.__duracao = duracao
        self.__custo_unitario = custo_unitario

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem: str):
        self.__origem = origem


    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino: str):
        self.__destino = destino

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: int):
        self.__duracao = duracao

    @property
    def custo_unitario(self):
        return self.__custo_unitario

    @custo_unitario.setter
    def custo_unitario (self, custo_unitario: int):
        self.__custo_unitario = custo_unitario

az = PacoteViagem('sdsd','usuus', 21, 100)

class Venda():

    def __init__(self, codigo: int, cliente: Cliente, descricao: str, pacote: PacoteViagem, quantidade: int):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__descricao = descricao
        self.__pacote = pacote
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def pacote(self):
        return self.__pacote

    @pacote.setter
    def pacote(self, pacote: PacoteViagem):
        self.__pacote = pacote

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    def preco_total(self):
        pacote = self.__quantidade
        precco = custo_unitario
        return pacote * 3

teste = Venda(123,'Berti','bom','sds',3)
test = teste.preco_total()





