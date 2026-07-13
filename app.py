from modelos.restaurante import Restaurante #usado para importar o codigo de outro repositorio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('paozinho', 2.00, 'o melhor pao da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()