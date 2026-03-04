"""
Módulo responsável pela gestão do carrinho de compras.

Este módulo define a classe Carrinho, que gerencia a lista de produtos,
cálculos de totais, descontos e persistência dos dados.
"""

from backend.produto import Produto
from dados.armazenamento_produtos import ArmazenamentoProdutos

class Carrinho():
    """
    Gerencia uma coleção de produtos e sua persistência.

    Esta classe atua como a lógica central para manipulação de itens no
    carrinho, permitindo adicionar, remover e realizar cálculos financeiros.

    Atributos:
    ----------
    lista_de_produtos : list[Produto]
        Lista contendo os objetos Produto atualmente no carrinho.
    __banco_de_dados : ArmazenamentoProdutos
        Instância para lidar com a persistência de dados em arquivo.
    """

    def __init__(self):
        """
        Inicializa o carrinho e carrega produtos previamente salvos.
        """
        self.__banco_de_dados = ArmazenamentoProdutos()
        self.lista_de_produtos:list[Produto] = []

        # Carregar dados anteriormente salvos.
        self.lista_de_produtos = self.__resgatar_produtos()

    def adicionar_produto(self, produto:Produto):
        """
        Adiciona um novo produto ao carrinho e persiste a alteração.

        Parâmetros:
        -----------
        produto : Produto
            O objeto produto a ser adicionado.
        """
        self.lista_de_produtos.append(produto)
        self.__salvar_carrinho()
        
    def remover_produto(self, nome_produto:str):
        """
        Remove um produto do carrinho pelo nome e persiste a alteração.

        Parâmetros:
        -----------
        nome_produto : str
            Nome do produto a ser removido (insensível a maiúsculas/minúsculas).
        """
        nome_produto = nome_produto.capitalize()
        
        for i, produto in enumerate(self.lista_de_produtos):
            if produto.nome == nome_produto:
                self.lista_de_produtos.pop(i)

        self.__salvar_carrinho()

    def calcular_total(self) -> float:
        """
        Calcula o valor total de todos os produtos no carrinho.

        Retorna:
        --------
        float
            A soma dos preços de todos os itens.
        """
        obter_preco = lambda x: x.preco
        lista_de_precos = map(obter_preco, self.lista_de_produtos)
        lista_de_precos = list(lista_de_precos)
        preco_total = sum(lista_de_precos)

        return preco_total

    def aplicar_desconto_em_produto(self, porcentagem_desconto:float, nome_produto:str):
        """
        Calcula o preço final de um produto específico após aplicar um desconto.

        Parâmetros:
        -----------
        porcentagem_desconto : float
            Valor do desconto em porcentagem (ex: 10 para 10%).
        nome_produto : str
            Nome do produto para aplicar o desconto.

        Retorna:
        --------
        float | None
            O novo preço com desconto aplicado ou None se o produto não for encontrado.
        """
        nome_produto = nome_produto.capitalize()
        produto_selecionado = None

        # Achar produto.
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
        """
        Verifica se um produto existe no carrinho pelo nome.

        Parâmetros:
        -----------
        nome_produto : str
            Nome do produto a ser verificado.

        Retorna:
        --------
        bool
            True se o produto estiver no carrinho, False caso contrário.
        """
        nome_produto = nome_produto.capitalize()

        # Procurar entres os produtos.
        for produto in self.lista_de_produtos:
            if produto.nome == nome_produto:
                return True

        # Se nome não encontrado...
        return False

    
    # Funções para interação com os dados.
    def __salvar_carrinho(self):
        """
        Converte a lista de objetos Produto em dicionários e salva no arquivo JSON.
        """
        # Função que transforma Produto em {"nome": nome, "preco": preco}
        # Necessário para salvar em um json.
        criar_dicionario_com_produto = lambda x: {"nome": x.nome,
                                                  "preco": x.preco}

        dicionarios_produto = map(
                criar_dicionario_com_produto,
                self.lista_de_produtos
        )
        dicionarios_produto = list(dicionarios_produto)

        # Escrever novo estado do Carrinho.
        self.__banco_de_dados.salvar_produtos(dicionarios_produto)

    def __resgatar_produtos(self):
        """
        Recupera os dados do arquivo JSON e os converte em instâncias de Produto.

        Retorna:
        --------
        list[Produto]
            Lista de objetos Produto recuperados.
        """
        # Função para processar dados vindos do json.
        mudar_dicionario_para_produto = \
            lambda x: Produto(x["nome"], x["preco"])
        
        produtos_salvos = self.__banco_de_dados.resgatar_produtos()

        # Transformar a lista de dicionários em lista de Produto.
        produtos_atuais = list(map(
            mudar_dicionario_para_produto,
            produtos_salvos
        ))
        
        return produtos_atuais
        
