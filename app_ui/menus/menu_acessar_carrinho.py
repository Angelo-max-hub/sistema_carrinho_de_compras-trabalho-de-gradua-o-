from core.criar_menu import criar_menu, Menu, Option, ControladorTela, InteracaoComUsuario
from backend.carrinho import Carrinho, Produto


class MenuCarrinho:
    def __init__(self, carrinho:Carrinho) -> None:
        self.__carrinho:Carrinho = carrinho
        self.__controlador = ControladorTela()
        
        # Menu de opções da tela.
        self.__menu = Menu(
            opcoes=[
                Option("Voltar", self.__sair),
                Option("Adicionar um Produto", self.__adicionar_novo_produto),
                Option("Ver produtos adicionados", self.__ver_produtos),
                Option("Remover um produto", self.__remover_produto)
            ],
            titulo_menu="Carrinho",
            funcao_inicial=None
        )

    def iniciar_menu(self):
        criar_menu(self.__menu)
        
            
    def __sair(self):
        return self.__controlador.SAIR

    def __adicionar_novo_produto(self):
        interacao = InteracaoComUsuario()

        # Interagir com o usuário.
        interacao.imprimir_cabecario("Adicionando produto...")
        nome_produto:str = interacao.obter_texto("Nome do produto:")
        preco_produto:float = interacao.obter_real("Preço do produto:")
        
        self.__carrinho.adicionar_produto(
            Produto(nome_produto, preco_produto)
        )
        print("O produto foi adicionado com sucesso!")
        self.__controlador.esperar(2)
        
    def __ver_produtos(self):
        print("Produtos adicionados ao carrinho:", end="\n\n")

        for produto in self.__carrinho.lista_de_produtos:
            print(f"- {produto.nome}")

        self.__controlador.esperar_enter()
        
    def __remover_produto(self):
        interacao = InteracaoComUsuario()

        # Entrada de dados..
        interacao.imprimir_cabecario("Removendo um produto...")
        nome_produto = interacao.obter_texto("Nome do produto:")
        
        if self.__carrinho.esta_em_carrinho(nome_produto):
            self.__carrinho.remover_produto(nome_produto)
        else:
            self.__controlador.exibir_mensagem_de_erro(
                "Não há produto com este nome!")
