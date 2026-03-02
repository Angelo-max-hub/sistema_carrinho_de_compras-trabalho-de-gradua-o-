from core.utils.controlador_tela import ControladorTela
import re
class InteracaoComUsuario:
    def __init__(self):
        # Expressão regular para validar entrada de reais (ex: 1,00)
        self.padrao_real = r"^\d+,\d{2}$"
        
    def imprimir_cabecario(self, titulo:str):
        print("\n", "= = = = = = = = = = =")
        print(titulo)
        print("Forneça as informações requisitadas.", "\n")

    def obter_real(self, requisicao:str) -> float:
        """Obriga o usuário a inserir no formato 'n,nn', onde 'n' é um número.
        Por exemplo, '1,00'.

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
        tipo_informativo = "número inteiro"
        entrada = self.__pedir_ao_usuario(requisicao, tipo_informativo)
        
        if entrada.isdigit():
            return int(entrada)
        else:
            self.__exibir_erro_de_entrada()
            return self.obter_inteiro(requisicao)


    def obter_texto(self, requisicao:str) -> str:
        tipo_informativo = "texto"
        entrada = self.__pedir_ao_usuario(requisicao, tipo_informativo)

        if entrada.isalpha():
            return entrada
        else:
            self.__exibir_erro_de_entrada()
            return self.obter_texto(requisicao)

    def formatar_numero_como_real(self, numero:float) -> str:
        """Formata um número como o real brasileiro, isto é, <n,nn> ou
        12,99"""

        numero = round(numero, 2)
        numero_str = str(numero).replace(".", ",")

        return numero_str
        
    # Funções auxiliares.
    def __pedir_ao_usuario(self, requisicao:str, tipo_entrada:str) -> str:
        print(requisicao)
        entrada = input(f"<{tipo_entrada}> ");

        return entrada

    def __exibir_erro_de_entrada(self):
        # Imprimir mensagem de erro e depois limpá-la.
        print("<RESPOSTA INVÁLIDA>", end="\r")
        ControladorTela().esperar(2)
        print("                   ", end="\r") 
    
