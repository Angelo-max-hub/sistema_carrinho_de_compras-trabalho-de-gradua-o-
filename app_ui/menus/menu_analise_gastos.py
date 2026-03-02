from backend.carrinho import Carrinho
from core.criar_menu import Menu, Option, ControladorTela, criar_menu, \
    InteracaoComUsuario
from core.utils import controlador_tela


class MenuAnaliseGastos:
    def __init__(self, carrinho:Carrinho) -> None:
        self.__controlador = ControladorTela()
        self.__carrinho = carrinho
        self.__menu = Menu(
            opcoes=[
                Option("Voltar", self.__sair),
                Option("Calcular total de gastos", self.__calcular_total),
                Option("Aplicar desconto em produto", self.__aplicar_desconto)
            ],
            titulo_menu="Análise de gastos.",
            funcao_inicial=None)


    def iniciar_menu(self):
        criar_menu(self.__menu)
        

    # Funçõs para as opções de menu.
    def __sair(self):
        return self.__controlador.SAIR
        
    def __calcular_total(self):
        custo_total = self.__carrinho.calcular_total()

        # Formatar custo total para real. (ex: 2,99)
        custo_total = round(custo_total, 2)
        custo_total = str(custo_total).replace(".", ",")
        
        # Limpar a tela e imprimir conteúdo.
        self.__controlador.limpar_tela()

        self.__controlador.imprimir_com_bordas(
            borda="==============================",
            mensagem=f"Custo total: {custo_total}"
        )

        self.__controlador.esperar_enter()

    def __aplicar_desconto(self):
        interacao_usuario = InteracaoComUsuario()

        # Interação com o usuário.
        nome_produto = interacao_usuario.obter_texto("nome do produto:")
        desconto_em_porcentagem = interacao_usuario.obter_real(
            "Desconto em porcetagem (ex: 5,04 / 60,71, sem o símbolo %):"
        )

        if self.__validar_desconto_e_produto(nome_produto, desconto_em_porcentagem):
            preco_final = self.__carrinho.aplicar_desconto_em_produto(
                float(desconto_em_porcentagem),
                nome_produto
            )
            self.__controlador.imprimir_com_bordas(
                "= = = = = = = = = = =",
                "Preço com desconto: {}".format(
                    interacao_usuario.formatar_numero_como_real(preco_final)
                )
            )
            self.__controlador.esperar_enter()
            
        else:
            self.__controlador.exibir_mensagem_de_erro(
                "Resposta inválida ou produto ausente..."
            )

            
    # Métodos auxiliares.
    def __validar_desconto_e_produto(self, nome_produto:str,
                                     desconto_em_porcentagem:float) -> bool:
        
        produto_existe = self.__carrinho.esta_em_carrinho(nome_produto)
        desconto_esta_correto = 0 <= desconto_em_porcentagem <= 100
        
        return produto_existe and desconto_esta_correto
