"""
Módulo de persistência de dados.

Este módulo contém a classe ArmazenamentoProdutos, responsável por gerenciar
a leitura e escrita de informações de produtos em um arquivo JSON.
"""

import json
from pathlib import Path


class ArmazenamentoProdutos:
    """
    Gerencia o armazenamento persistente de produtos em formato JSON.

    Esta classe lida com as operações de baixo nível de sistema de arquivos,
    garantindo que os dados do carrinho sejam preservados entre sessões.

    Atributos:
    ----------
    arquivo_json : Path
        Caminho para o arquivo JSON onde os dados são armazenados.
    """

    def __init__(self) -> None:
        """
        Inicializa o sistema de armazenamento e cria o arquivo se necessário.
        """
        # Nome do arquivo de dados.
        nome_arquivo = "produtos.json"
        
        self.arquivo_json = Path(f"dados/{nome_arquivo}")

        # Criar arquivo de armazenamento se não existente.
        if not self.arquivo_json.exists():
            self.arquivo_json.write_text("")

        
    def salvar_produtos(self, dados_produtos:list[dict[str, float]]):
        """
        Salva dados básicos dos produtos em um arquivo JSON.

        Parâmetros:
        -----------
        dados_produtos : list[dict]
            Lista com os nomes e preços dos produtos. Cada produto deve ser um
            dicionário {'nome': nome, 'preco': preco}.
        """
        dados_compilados = json.dumps(dados_produtos)
        self.arquivo_json.write_text(dados_compilados)

    def resgatar_produtos(self) -> list[dict[str, str | float]]:
        """
        Recupera os dados dos produtos do arquivo JSON.

        Retorna:
        --------
        list[dict]
            Lista de dicionários contendo os dados dos produtos ou uma lista
            vazia se o arquivo estiver em branco.
        """
        dados_compilados = self.arquivo_json.read_text()

        # Verificar se o conteúdo do arquivo está vazio.
        if dados_compilados:
            dados_processados = json.loads(dados_compilados)
            
            return dados_processados
        else:
            return []
