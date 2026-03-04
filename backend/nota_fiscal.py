"""
Módulo responsável pela geração de notas fiscais.

Este módulo define a classe NotaFiscal, que formata e exibe os dados
dos produtos contidos em um carrinho para o usuário.
"""

from backend.carrinho import Carrinho

class NotaFiscal:
    """
    Representa a nota fiscal de uma compra.

    Esta classe processa um objeto Carrinho para exibir uma listagem
    formatada de produtos e seus respectivos preços.

    Atributos:
    ----------
    lista_produtos : list
        Lista de produtos obtida do carrinho.
    SEPARADOR : str
        String utilizada para formatar a saída visual da nota fiscal.
    """

    def __init__(self, carrinho: Carrinho):
        """
        Inicializa a nota fiscal com base em um carrinho de compras.

        Parâmetros:
        -----------
        carrinho : Carrinho
            O objeto carrinho contendo os produtos para a nota.
        """
        self.lista_produtos = carrinho.lista_de_produtos
        self.SEPARADOR = "------------------------"

    def gerar_nota_fiscal(self):
        """
        Imprime a nota fiscal formatada no terminal.
        """
        print("NOTA FISCAL", end="\n\n")
        print(f"Nome {self.SEPARADOR} Preço")
        for produto in self.lista_produtos:
            print(f"{produto.nome} {self.SEPARADOR} {produto.preco}")
