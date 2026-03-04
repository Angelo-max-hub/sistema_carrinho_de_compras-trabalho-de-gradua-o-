"""
Módulo orquestrador de menus.

Este módulo fornece a função criar_menu, que é responsável por manter o
ciclo de vida de um menu no terminal, gerenciando o loop de exibição.
"""

from core.menu import Menu
from core.utils.option import Option
from core.utils.controlador_tela import ControladorTela
from core.interacao_usuario import InteracaoComUsuario

def criar_menu(menu: Menu):
    """
    Mantém um menu em execução dentro de um loop contínuo.

    Esta função renderiza repetidamente o menu fornecido até que uma de suas
    opções retorne o sinal "SAIR" (ControladorTela.SAIR).

    Parâmetros:
    -----------
    menu : Menu
        O objeto Menu que será exibido e gerenciado no loop.
    """
    controlador = ControladorTela()
    while True:
        resultado = menu.exibir_menu_e_obter_resposta()
        if resultado == controlador.SAIR:
            break
