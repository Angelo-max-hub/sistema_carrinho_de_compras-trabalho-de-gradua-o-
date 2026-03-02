import os
import platform
import time

class ControladorTela:
    def __init__(self) -> None:
        self.SAIR = "SAIR"

    def limpar_tela(self):
        "Função multiplatarforma para limpar o terminal"
        if platform.system == "Windows":
            os.system("cls")
        else:
            os.system("clear")
            
    def esperar_enter(self):
        input("Aperte <ENTER> para continuar...   ")

    def esperar(self, espera:int):
        time.sleep(espera)

    def imprimir_com_bordas(self, borda:str, mensagem:str):
        print(borda)
        print(mensagem)
        print(borda)

    def exibir_mensagem_de_erro(self, mensagem:str):
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
