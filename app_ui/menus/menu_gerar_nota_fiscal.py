from core.criar_menu import criar_menu, ControladorTela, Option, Menu
from backend.nota_fiscal import NotaFiscal

class MenuNotaFiscal:
    def __init__(self, nota_fiscal:NotaFiscal) -> None:
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
        criar_menu(self.__menu)

    # Opções de menu.
    def __sair(self):
        return ControladorTela().SAIR

    def __gerar_nota_fiscal(self):
        self.__nota_fiscal.gerar_nota_fiscal()
        self.controlador.esperar_enter()
        
