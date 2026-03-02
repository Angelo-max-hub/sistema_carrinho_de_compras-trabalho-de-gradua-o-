from os import listxattr
from core.utils.option import Option
from core.utils.controlador_tela import ControladorTela

# Constante para sinalizar que o menu deve ser fechado.
SAIR = "SAIR"

class Menu:
    """Classe para criação de menus de terminal.

    Permite criar menus funcionais sem necessidade de estruturas condicionais ou 'prints'
    concecutivos.

    Notes:
       Para renderizar um menu, é absolutamente necessário usar uma instância dessa classe
       juntamente com a função <criar_menu>, em <core/criar_menu.py>. Ela cuida da criação e
       e gerenciamento de um loop para o menu não se desfazer. Dessa maneira:
       criar_menu(Menu(...)), onde '...' são os argumentos da classe.
    """

    def __init__(self, opcoes:list[Option], titulo_menu:str,
                 funcao_inicial=None):
        self.__opcoes = opcoes
        self._funcao_inicial = funcao_inicial # função executada ao abrir o menu.
        self.__titulo_menu = titulo_menu
        self._controlador = ControladorTela()
            
    def exibir_menu_e_obter_resposta(self):
        """
        Cria um menu de terminal e executa ações com base nas opções fornecidas.
        """
        # Limpar a tela e imprimir título do menu.
        self._controlador.limpar_tela()
        print(self.__titulo_menu + "\n\n")
        
        # Executar a função inicial, se fornecida pelo chamador.
        if self._funcao_inicial:
            self._funcao_inicial()

        # Mostrar o menu.
        self.__exibir_menu()        

        # Tratar e reagir a entrada do usuário.
        numero_fornecido = self.__obter_entrada_usuario()
        if numero_fornecido is None:
            self._controlador.exibir_mensagem_de_erro("RESPOSTA INVÁLIDA!")
        else:
            # Executar a função associada a opção escolhida.
            # O retorno será um sinal para função de controle de loop.
            return self.__opcoes[numero_fornecido].acao()


    def __obter_entrada_usuario(self) -> int | None:
        numero_opcoes = len(self.__opcoes)
        
        # Obter entrada do usuário.
        numero_dado = input("<insira aqui> ")

        # Retornar índice fornecido se for um número inteiro e
        # opção existente.
        if not numero_dado.isdigit():
            return None

        if not int(numero_dado) in range(0, numero_opcoes):
            return None

        return int(numero_dado)
        
    def __exibir_menu(self):
        for i, opcao in enumerate(self.__opcoes):
            print(f"{i} - {opcao.titulo}")
