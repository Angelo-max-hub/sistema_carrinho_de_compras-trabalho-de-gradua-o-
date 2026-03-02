from core.criar_menu import criar_menu, Menu, Option, ControladorTela
from app_ui.menus.menu_acessar_carrinho import MenuCarrinho
from app_ui.menus.menu_analise_gastos import MenuAnaliseGastos
from app_ui.menus.menu_gerar_nota_fiscal import MenuNotaFiscal
from backend.carrinho import Carrinho
from backend.nota_fiscal import NotaFiscal

class MenuPrincipal:
    def __init__(self) -> None:
        self.__controlador = ControladorTela()
        carrinho = Carrinho()
        gerador_nota_fiscal = NotaFiscal(carrinho)
        # Menus.
        menu_acessa_carrinho = MenuCarrinho(carrinho)
        menu_analise_gastos = MenuAnaliseGastos(carrinho)
        menu_nota_fiscal = MenuNotaFiscal(gerador_nota_fiscal)

        # Configurar o menu principal.
        self.__menu = Menu(
            opcoes=[
                Option("Sair", self.__sair),
                Option("Acessar carrinho", menu_acessa_carrinho.iniciar_menu),
                Option("Análise de gastos", menu_analise_gastos.iniciar_menu),
                Option("Gerar nota fiscal", menu_nota_fiscal.iniciar_menu)
        ],
            titulo_menu="Menu principal do sistema de compras.",
            funcao_inicial=None
)
    def iniciar_menu_principal(self):
        criar_menu(self.__menu)
        
    def __sair(self):
        return self.__controlador.SAIR
