from core.menu import Menu
from core.utils.option import Option
from core.utils.controlador_tela import ControladorTela
from core.interacao_usuario import InteracaoComUsuario

def criar_menu(menu:Menu):
    controlador = ControladorTela()
    while True:
        resultado = menu.exibir_menu_e_obter_resposta()
        if resultado == controlador.SAIR:
            break
