"""
Módulo de definição da interface de menu.

Este módulo contém a classe Menu, que estrutura a exibição de opções
e o processamento da escolha do usuário no terminal.
"""

from core.utils.option import Option
from core.utils.controlador_tela import ControladorTela

class Menu:
    """
    Representa um menu interativo no terminal.

    Permite configurar um título, uma lista de opções (Option) e uma função
    opcional de inicialização. Funciona em conjunto com a função `criar_menu`.

    Atributos:
    ----------
    __opcoes : list[Option]
        Lista de objetos Option que compõem as entradas do menu.
    _funcao_inicial : callable | None
        Função opcional executada sempre que o menu é renderizado.
    __titulo_menu : str
        Título exibido no topo do menu.
    _controlador : ControladorTela
        Instância para manipulação da tela do terminal.
    """

    def __init__(self, opcoes:list[Option], titulo_menu:str,
                 funcao_inicial=None):
        """
        Inicializa a estrutura de um menu.

        Parâmetros:
        -----------
        opcoes : list[Option]
            Lista de opções disponíveis para o usuário.
        titulo_menu : str
            Texto que aparecerá como cabeçalho do menu.
        funcao_inicial : callable, opcional
            Função a ser chamada antes de exibir as opções.
        """
        self.__opcoes = opcoes
        self._funcao_inicial = funcao_inicial
        self.__titulo_menu = titulo_menu
        self._controlador = ControladorTela()
            
    def exibir_menu_e_obter_resposta(self):
        """
        Renderiza o menu na tela e processa a ação da opção escolhida.

        Limpa a tela, executa a função inicial (se houver), lista as opções
        e aguarda a entrada do usuário para disparar a ação correspondente.

        Retorna:
        --------
        Any
            O valor de retorno da ação associada à opção escolhida (ex: "SAIR").
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
        """
        Solicita e valida o índice da opção escolhida pelo usuário.

        Retorna:
        --------
        int | None
            O índice da opção se for válido, ou None se for inválido.
        """
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
        """
        Imprime as opções numeradas do menu no terminal.
        """
        for i, opcao in enumerate(self.__opcoes):
            print(f"{i} - {opcao.titulo}")
