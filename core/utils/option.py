"""
Módulo utilitário para itens de menu.

Este módulo define a classe Option, que associa um título a uma
ação executável em um menu.
"""

from types import FunctionType, MethodType


class Option:
    """
    Representa uma opção selecionável em um menu.

    Atributos:
    ----------
    titulo : str
        O texto que será exibido para a opção no menu.
    acao : FunctionType | MethodType
        A função ou método que será executado quando a opção for selecionada.
    """

    def __init__(self, titulo: str, acao: FunctionType | MethodType):
        """
        Inicializa uma nova opção de menu.

        Parâmetros:
        -----------
        titulo : str
            Título da opção.
        acao : FunctionType | MethodType
            Função a ser executada ao selecionar a opção.
        """
        self.titulo = titulo
        self.acao = acao
