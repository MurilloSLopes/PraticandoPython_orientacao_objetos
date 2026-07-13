from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante: #criando uma classe
    """Representa um restaurante e suas características."""

    restaurantes = [] #criando uma lista para armazenar os restaurantes   

    def __init__(self, nome, categoria): #criando o metodo construtor(init sempre que quero definir um valor fixo)
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title() #deixa o metodo com a primeira leta maiscula - (.title())
        self.categoria = categoria.upper() #deixa o metodo com todas as letras maiusculas - (.upper())
        self._ativo = False #usando o underline para definir que o atributo é privado (_ativo)
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) #adicionando o restaurante na lista de restaurantes

    def __str__(self): #criando o metodo str para retornar uma string com os valores dos atributos da classe
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self.categoria}'
    
    @classmethod # usando o decorator @classmethod para criar um metodo de classe que pode ser chamado sem instanciar a classe
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}') #retornando os valores dos atributos da classe
        for restaurante in cls.restaurantes: #puxando os restaurantes da lista restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') #retornando os valores dos atributos da classe

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return 'Verdadeiro' if self._ativo else "falso"
    
    def alterar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'cardapio do restaurant {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. nome: {item._nome} | preco: R${item._preco} | descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. nome: {item._nome} | preco: R${item._preco} | tamanho: {item.tamanho}'
                print(mensagem_bebida)

