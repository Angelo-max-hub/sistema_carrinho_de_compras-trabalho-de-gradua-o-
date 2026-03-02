from backend.carrinho import Carrinho

class NotaFiscal:
    def __init__(self, carrinho:Carrinho):
        self.lista_produtos = carrinho.lista_de_produtos
        self.SEPARADOR = "------------------------"

    def gerar_nota_fiscal(self):
        print("NOTA FISCAL", end="\n\n")
        print(f"Nome {self.SEPARADOR} Preço")
        for produto in self.lista_produtos:
            print(f"{produto.nome} {self.SEPARADOR} {produto.preco}")
