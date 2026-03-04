"""
Módulo de interface para análise financeira do carrinho.

Este módulo contém a classe MenuAnaliseGastos, que permite calcular totais
e simular a aplicação de descontos em produtos específicos.
"""

from backend.carrinho import Carrinho
from core.criar_menu import Menu, Option, ControladorTela, criar_menu, \
    InteracaoComUsuario


class MenuAnaliseGastos:
    """
    Interface de terminal para cálculos e descontos.

    Fornece ferramentas visuais para o usuário visualizar o custo total da compra
    e aplicar porcentagens de desconto sobre itens do carrinho.

    Atributos:
    ----------
    __controlador : ControladorTela
        Controlador para operações de tela.
    __carrinho : Carrinho
        Instância do carrinho para consulta de valores.
    __menu : Menu
        O objeto de menu estruturado com as opções de análise.
    """

    def __init__(self, carrinho:Carrinho) -> None:
        """
        Inicializa o menu de análise de gastos.

        Parâmetros:
        -----------
        carrinho : Carrinho
            O objeto carrinho que será analisado.
        """
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
        """
        Inicia o loop de exibição do menu de análise.
        """
        criar_menu(self.__menu)
        

    # Funçõs para as opções de menu.
    def __sair(self):
        """
        Sinaliza o encerramento do menu atual.

        Retorna:
        --------
        str
            Sinal de saída (SAIR).
        """
        return self.__controlador.SAIR
        
    def __calcular_total(self):
        """
        Calcula e exibe o custo total dos produtos no carrinho.
        """
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
        """
        Interage com o usuário para aplicar um desconto a um produto e exibe o resultado.
        """
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
        """
        Verifica se o produto existe e se o valor do desconto é válido.

        Parâmetros:
        -----------
        nome_produto : str
            Nome do produto a ser verificado.
        desconto_em_porcentagem : float
            Valor da porcentagem (deve estar entre 0 e 100).

        Retorna:
        --------
        bool
            True se os dados forem válidos, False caso contrário.
        """
        
        produto_existe = self.__carrinho.esta_em_carrinho(nome_produto)
        desconto_esta_correto = 0 <= desconto_em_porcentagem <= 100
        
        return produto_existe and desconto_esta_correto
