from modelos.avaliacao import Avaliacao

class Restaurante: #criando uma classe
    restaurantes = [] #criando uma lista para armazenar os restaurantes   

    def __init__(self, nome, categoria): #criando o metodo construtor(init sempre que quero definir um valor fixo)
        self._nome = nome.title() #deixa o metodo com a primeira leta maiscula - (.title())
        self.categoria = categoria.upper() #deixa o metodo com todas as letras maiusculas - (.upper())
        self._ativo = False #usando o underline para definir que o atributo é privado (_ativo)
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #adicionando o restaurante na lista de restaurantes

    def __str__(self): #criando o metodo str para retornar uma string com os valores dos atributos da classe
        return f'{self._nome} | {self.categoria}'
    
    @classmethod # usando o decorator @classmethod para criar um metodo de classe que pode ser chamado sem instanciar a classe
    def listar_restaurantes(cls): 
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}') #retornando os valores dos atributos da classe
        for restaurante in cls.restaurantes: #puxando os restaurantes da lista restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') #retornando os valores dos atributos da classe

    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else "falso"
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media