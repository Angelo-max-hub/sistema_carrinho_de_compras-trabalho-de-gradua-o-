"""
Módulo de interface para emissão de nota fiscal.

Este módulo contém a classe MenuNotaFiscal, que gerencia a exibição
e geração do comprovante de compra.
"""

from core.criar_menu import criar_menu, ControladorTela, Option, Menu
from backend.nota_fiscal import NotaFiscal

class MenuNotaFiscal:
    """
    Interface de terminal para geração de nota fiscal.

    Atributos:
    ----------
    controlador : ControladorTela
        Controlador para operações de tela.
    __nota_fiscal : NotaFiscal
        Instância de NotaFiscal que será processada.
    __menu : Menu
        O objeto de menu estruturado com as opções de nota fiscal.
    """

    def __init__(self, nota_fiscal:NotaFiscal) -> None:
        """
        Inicializa o menu de nota fiscal.

        Parâmetros:
        -----------
        nota_fiscal : NotaFiscal
            O objeto NotaFiscal para geração do comprovante.
        """
        self.controlador = ControladorTela()
        self.__nota_fiscal = nota_fiscal
        self.__menu = Menu(
            opcoes=[
                Option("Voltar", self.__sair),
                Option("Gerar nota fiscal", self.__gerar_nota_fiscal)
            ],
            titulo_menu="Nota fiscal"
        )

    def iniciar_menu(self):
        """
        Inicia o loop de exibição do menu de nota fiscal.
        """
        criar_menu(self.__menu)

    # Opções de menu.
    def __sair(self):
        """
        Sinaliza o encerramento do menu atual.

        Retorna:
        --------
        str
            Sinal de saída (SAIR).
        """
        return ControladorTela().SAIR

    def __gerar_nota_fiscal(self):
        """
        Aciona a lógica de geração de nota fiscal e aguarda confirmação.
        """
        self.__nota_fiscal.gerar_nota_fiscal()
        self.controlador.esperar_enter()
