"""
Módulo responsável pela definição da classe Produto.

Este módulo contém a representação básica de um produto no sistema,
armazenando informações como nome e preço.
"""

class Produto:
    """
    Representa um item disponível para compra.

    Atributos:
    ----------
    nome : str
        O nome do produto, formatado com a primeira letra maiúscula.
    preco : float
        O valor unitário do produto.
    """

    def __init__(self, nome: str, preco: float):
        """
        Inicializa um novo produto.

        Parâmetros:
        -----------
        nome : str
            Nome do produto.
        preco : float
            Preço do produto.
        """
        self.nome = nome.capitalize()
        self.preco = preco
