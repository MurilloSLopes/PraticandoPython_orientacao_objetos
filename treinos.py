'''
##Atividade 1 - Criando uma classe Musica com atributos nome, artista e duracao

class Musica: #criacao de classe
    nome = ''
    artista = ''
    duracao = int

# dando valores para os atributos da classe
musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234
'''



'''
##Atividade 2 - Refatorando a classe Musica para utilizar o metodo construtor

class Musica:
    def __init__(self, nome = '' , artista = '', duracao=0): #criando o metodo construtor e definindo valores padroes para os atributos da classe
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)
'''



'''
##Atividade 3 - refatorando funçoes adicionando atributos e medotos especiais

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1
# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
'''


'''
#Atividade 4

# 1) Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

# 2) Na classe Livro, adicione um método especial __str__ que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

print(livro1)
print(livro2)

# 3) Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

# 4) Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros

# 5) Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# 6) No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")

# 8) Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método __str__.
from minha_classe import Livro  # Certifique-se de corrigir o nome do arquivo para o correto

livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)

print(livro_main1)
print(livro_main2)
'''


'''
## 1- Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

## 2- Construa o Método Especial __str__: Adicione um método especial __str__ à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Status: {status}"

## 3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

## 4- Implemente o Método Especial __str__ na Classe Filha: Adicione um método especial __str__ à classe Carro que estenda o método da classe pai (Veiculo).

def __str__(self):
    return f"{super().__str__()} - Portas: {self.portas}"

## 5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

## 6- Implemente o Método Especial __str__ na Classe Filha (Moto): Adicione um método especial __str__ à classe Moto que estenda o método da classe pai (Veiculo).

def __str__(self):
    return f"{super().__str__()} - Tipo: {self.tipo}"

## 7- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

## 8- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

from carros import Carro
from motos import Moto

carro1 = Carro("Toyota", "Corolla", 4)
carro2 = Carro("Honda", "Civic", 2)
carro3 = Carro("Ford", "Fusion", 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")

## 9- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método __str__.

print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)
'''