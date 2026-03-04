"""
Módulo para gerenciamento de entradas e saídas do usuário.

Este módulo define a classe InteracaoComUsuario, que lida com a coleta,
validação e formatação de dados inseridos pelo usuário no terminal.
"""

from core.utils.controlador_tela import ControladorTela
import re

class InteracaoComUsuario:
    """
    Gerencia a comunicação direta com o usuário via terminal.

    Fornece métodos para solicitar diferentes tipos de dados (inteiros, reais, texto)
    com validação automática e formatação de saída.

    Atributos:
    ----------
    padrao_real : str
        Expressão regular para validar o formato de moeda real (ex: 1,00).
    """

    def __init__(self):
        """
        Inicializa a classe de interação com as configurações de validação.
        """
        # Expressão regular para validar entrada de reais (ex: 1,00)
        self.padrao_real = r"^\d+,\d{2}$"
        
    def imprimir_cabecario(self, titulo:str):
        """
        Exibe um cabeçalho padronizado para solicitações de dados.

        Parâmetros:
        -----------
        titulo : str
            O título da seção ou formulário atual.
        """
        print("\n", "= = = = = = = = = = =")
        print(titulo)
        print("Forneça as informações requisitadas.", "\n")

    def obter_real(self, requisicao:str) -> float:
        """
        Solicita e valida um valor numérico no formato de Real (R$).

        Obriga o usuário a inserir no formato 'n,nn', onde 'n' é um número.
        Exemplo: '1,00'. Se a entrada for inválida, solicita novamente.

        Parâmetros:
        -----------
        requisicao : str
            A mensagem de instrução para o usuário.

        Retorna:
        --------
        float
            O valor convertido para ponto flutuante.
        """
        tipo_informativo = "real (vírgula e 2 casas decimais. Assim: 2,99)"
        entrada = self.__pedir_ao_usuario(requisicao, tipo_informativo)

        # Tirar espaços.
        entrada = entrada.strip()
        
        if re.match(r"^\d+,\d{2}$", entrada):
            # Float não entende vírgulas corretamente.
            entrada = entrada.replace(",", ".")
            
            return float(entrada)
        else:
            self.__exibir_erro_de_entrada()
            return self.obter_real(requisicao)
    
    def obter_inteiro(self, requisicao:str) -> int:
        """
        Solicita e valida a entrada de um número inteiro.

        Parâmetros:
        -----------
        requisicao : str
            A mensagem de instrução para o usuário.

        Retorna:
        --------
        int
            O número inteiro validado.
        """
        tipo_informativo = "número inteiro"
        entrada = self.__pedir_ao_usuario(requisicao, tipo_informativo)
        
        if entrada.isdigit():
            return int(entrada)
        else:
            self.__exibir_erro_de_entrada()
            return self.obter_inteiro(requisicao)


    def obter_texto(self, requisicao:str) -> str:
        """
        Solicita e valida a entrada de um texto (apenas letras).

        Parâmetros:
        -----------
        requisicao : str
            A mensagem de instrução para o usuário.

        Retorna:
        --------
        str
            O texto validado.
        """
        tipo_informativo = "texto"
        entrada = self.__pedir_ao_usuario(requisicao, tipo_informativo)

        if entrada.isalpha():
            return entrada
        else:
            self.__exibir_erro_de_entrada()
            return self.obter_texto(requisicao)

    def formatar_numero_como_real(self, numero:float) -> str:
        """
        Converte um float para uma string formatada como Real brasileiro.

        Parâmetros:
        -----------
        numero : float
            O número a ser formatado.

        Retorna:
        --------
        str
            O número formatado (ex: "12,99").
        """

        numero = round(numero, 2)
        numero_str = str(numero).replace(".", ",")

        return numero_str
        
    # Funções auxiliares.
    def __pedir_ao_usuario(self, requisicao:str, tipo_entrada:str) -> str:
        """
        Método interno para realizar o input básico.

        Parâmetros:
        -----------
        requisicao : str
            A pergunta ao usuário.
        tipo_entrada : str
            Dica visual do tipo de dado esperado.

        Retorna:
        --------
        str
            A entrada bruta do usuário.
        """
        print(requisicao)
        entrada = input(f"<{tipo_entrada}> ");

        return entrada

    def __exibir_erro_de_entrada(self):
        """
        Exibe uma mensagem temporária de erro de entrada no terminal.
        """
        # Imprimir mensagem de erro e depois limpá-la.
        print("<RESPOSTA INVÁLIDA>", end="\r")
        ControladorTela().esperar(2)
        print("                   ", end="\r") 
    
