"""
Módulo utilitário para controle da interface de terminal.

Este módulo contém ferramentas para manipulação da tela do terminal,
como limpeza de tela, pausas e exibição de mensagens formatadas.
"""

import os
import platform
import time

class ControladorTela:
    """
    Controla operações de visualização e fluxo no terminal.

    Fornece métodos multiplataforma para interagir com o terminal do usuário.

    Atributos:
    ----------
    SAIR : str
        Constante utilizada para sinalizar o encerramento de um menu.
    """

    def __init__(self) -> None:
        """
        Inicializa o controlador de tela com constantes de controle.
        """
        self.SAIR = "SAIR"

    def limpar_tela(self):
        """
        Limpa o terminal de forma multiplataforma (Windows e Linux/Unix).
        """
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
            
    def esperar_enter(self):
        """
        Pausa a execução do programa até que o usuário pressione ENTER.
        """
        input("Aperte <ENTER> para continuar...   ")

    def esperar(self, espera:int):
        """
        Pausa a execução do programa por um tempo determinado.

        Parâmetros:
        -----------
        espera : int
            Tempo de espera em segundos.
        """
        time.sleep(espera)

    def imprimir_com_bordas(self, borda:str, mensagem:str):
        """
        Imprime uma mensagem cercada por bordas decorativas.

        Parâmetros:
        -----------
        borda : str
            A string que será usada como delimitador superior e inferior.
        mensagem : str
            A mensagem a ser exibida.
        """
        print(borda)
        print(mensagem)
        print(borda)

    def exibir_mensagem_de_erro(self, mensagem:str):
        """
        Exibe uma mensagem de erro visualmente destacada e limpa a tela.

        Parâmetros:
        -----------
        mensagem : str
            A descrição do erro a ser exibida.
        """
        self.limpar_tela()
        delimitador = \
            """
            =================================================================
                ERRO                 ERRO                 ERRO
            =================================================================
            """
        janela = \
            f"""
            {delimitador}
            {mensagem.upper()}
            {delimitador}
            """
        print(janela)
        time.sleep(2)
