from backend.produto import Produto
from dados.armazenamento_produtos import ArmazenamentoProdutos

class Carrinho():
    def __init__(self):
        self.__banco_de_dados = ArmazenamentoProdutos()
        self.lista_de_produtos:list[Produto] = []

        # Carregar dados anteriormente salvos.
        self.lista_de_produtos = self.__resgatar_produtos()

    def adicionar_produto(self, produto:Produto):
        self.lista_de_produtos.append(produto)
        self.__salvar_carrinho()
        
    def remover_produto(self, nome_produto:str):
        nome_produto = nome_produto.capitalize()
        
        for i, produto in enumerate(self.lista_de_produtos):
            if produto.nome == nome_produto:
                self.lista_de_produtos.pop(i)

        self.__salvar_carrinho

    def calcular_total(self) -> float:
        obter_preco = lambda x: x.preco
        lista_de_precos = map(obter_preco, self.lista_de_produtos)
        lista_de_precos = list(lista_de_precos)
        preco_total = sum(lista_de_precos)

        return preco_total

    def aplicar_desconto_em_produto(self, porcentagem_desconto:float, nome_produto:str):
        nome_produto = nome_produto.capitalize()
        produto_selecionado = None
        for produto in self.lista_de_produtos:
            if produto.nome == nome_produto:
                produto_selecionado = produto
                break
        else:
            return
        
        desconto_em_decimal = porcentagem_desconto / 100
        desconto_em_reais = produto_selecionado.preco * desconto_em_decimal
        preco_final = produto_selecionado.preco - desconto_em_reais

        return preco_final
    
    def esta_em_carrinho(self, nome_produto:str) -> bool:
        nome_produto = nome_produto.capitalize()
        for produto in self.lista_de_produtos:
            if produto.nome == nome_produto:
                return True

        # Se nome não encontrado...
        return False

    # Funções para interação com os dados.
    def __salvar_carrinho(self):
        # Função que transforma Produto em {"nome": nome, "preco": preco}
        # Necessário para salvar em um json.
        criar_dicionario_com_produto = lambda x: {"nome": x.nome,
                                                  "preco": x.preco}

        dicionarios_produto = map(
                criar_dicionario_com_produto,
                self.lista_de_produtos
        )
        dicionarios_produto = list(dicionarios_produto)
        
        self.__banco_de_dados.salvar_produtos(dicionarios_produto)

    def __resgatar_produtos(self):
        # Função para processar dados vindos do json.
        mudar_dicionario_para_produto = \
            lambda x: Produto(x["nome"], x["preco"])
        
        produtos_salvos = self.__banco_de_dados.resgatar_produtos()
        produtos_atuais = list(map(
            mudar_dicionario_para_produto,
            produtos_salvos
        ))
        
        return produtos_atuais
        
