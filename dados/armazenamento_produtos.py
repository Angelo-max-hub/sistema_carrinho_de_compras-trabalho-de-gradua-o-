import json
from pathlib import Path


class ArmazenamentoProdutos:
    def __init__(self) -> None:
        # Nome do arquivo de dados.
        nome_arquivo = "produtos.json"
        
        self.arquivo_json = Path(f"dados/{nome_arquivo}")

        # Criar arquivo de armazenamento se não existente.
        if not self.arquivo_json.exists():
            self.arquivo_json.write_text("")

        
    def salvar_produtos(self, dados_produtos:list[dict[str, float]]):
        """Salva dados básicos dos produtos em um arquivo json gerido
            internamente.
            
            Args:
            dados_produtos (list[dict]): lista com os nomes e preços dos
            produtos. Cada produto deve ser um dicionário
            {'nome': nome, 'preco': preco}.
            """
        dados_compilados = json.dumps(dados_produtos)
        self.arquivo_json.write_text(dados_compilados)

    def resgatar_produtos(self) -> list[dict[str, str | float]]:
        dados_compilados = self.arquivo_json.read_text()

        # Verificar se o conteúdo do arquivo está vazio.
        if dados_compilados:
            dados_processados = json.loads(dados_compilados)
            
            return dados_processados
        else:
            return []
