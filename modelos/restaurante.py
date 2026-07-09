class Restaurante: #criando uma classe
    restaurantes = [] #criando uma lista para armazenar os restaurantes   

    def __init__(self, nome, categoria): #criando o metodo construtor(init sempre que quero definir um valor fixo)
        self._nome = nome.title() #deixa o metodo com a primeira leta maiscula - (.title())
        self.categoria = categoria.upper() #deixa o metodo com todas as letras maiusculas - (.upper())
        self._ativo = False #usando o underline para definir que o atributo é privado (_ativo)
        Restaurante.restaurantes.append(self) #adicionando o restaurante na lista de restaurantes

    def __str__(self): #criando o metodo str para retornar uma string com os valores dos atributos da classe
        return f'{self._nome} | {self.categoria}'
    
    @classmethod # usando o decorator @classmethod para criar um metodo de classe que pode ser chamado sem instanciar a classe
    def listar_restaurantes(cls): 
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}') #retornando os valores dos atributos da classe
        for restaurante in cls.restaurantes: #puxando os restaurantes da lista restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}') #retornando os valores dos atributos da classe

    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else "falso"
    
    def alterar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes() #chamando o metodo listar_restaurantes para listar os restaurantes cadastrados