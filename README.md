# Introdução.
O programa contido neste repositório é a solução para um trabalho de graduação no curso
Tecnólogo em Análise e Desenvolvimento de Sistemas. Consiste em criar um programa em Python
simples que simula um sistema de carrinho, com o qual o usuário pode adicionar produtos e
realizar tarefas relacionadas a um sistema deste tipo, como calcular total de custo ou
imprimir nota fiscal.  Este trabalho foi pensado para fixação de conceitos de orientação a
objetos na disciplina "Linguagem de Programação II".

A seguir, mais sobre a implementação, arquitetura, instalação e uso do sistema, que, aliás,
não possui interface gráfica.

## Visão geral do sistema.
Como o programa não se propõe a ter uma interface gráfica --- não era necessário para se
adquirir uma nota 100 ---, ele conta com vários menus de terminal. Estes menus são
simplesmente opções imprimidas no terminal e "inputs" Python que esperam e processam
entradas do usuário. 

A implementação Python básica disso envolve várias "prints", "inputs" e conversões de e
para string, de maneira que a criação dos vários menus do sistema geraria muita duplicação
de código, além de mudanças globais se tornarem muita cansativas. Por exemplo, se eu, o
desenvolvedor, desejasse adicionar uma linha delimitadora entre as opções do menu e a
resposta do usuário, seria obrigado a ir vários arquivos diferentes, ou a vários pontos do
mesmo arquivo, adicionar o seguinte:

``` python
print("===============================================")
```

Decidi que isso era deselegante e não escalável, e por isso criei abstrações que tornavam
a criação de menus, opções, entradas de usuário e controle da tela automáticas e mais 
fáceis, embora *um pouco imperfeitas*, pois ainda precisam de alguma refatoração. A seguir
um exemplo real da criação de um menu perfeitamente funcional utilizando as abstrações que 
criei:

``` python
self.__menu = Menu(
            opcoes=[
                Option("Voltar", self.__sair),
                Option("Adicionar um Produto", self.__adicionar_novo_produto),
                Option("Ver produtos adicionados", self.__ver_produtos),
                Option("Remover um produto", self.__remover_produto)
            ],
            titulo_menu="Carrinho",
            funcao_inicial=None
        )
```

A implementação dessas abstrações adicionais estão contidas em "\core" e há mais sobre seu
uso não sessão **Usando as abstrações de menu** neste arquivo.

Este sistema é capaz de se lembrar das informações que o usuário adiciona. Essas
informações apenas podem ser os nomes e os preços dos produtos incluídos. Portanto, os
produtos não somem entre as execuções. E isso é possível graças ao arquivo json e código
Python contido em "dados/"

# Um pouco sobre a arquitetura.
A organização de pastas deste projeto foi um pouco inspirada no padrão **MMVC**, isto é,
há uma divisão do sistema entre **Dados**, **Lógica de negócios** e **Interface gráfica**.
Esses componentes possuem cada um diretório neste sistema, dessa maneira:

|      Componentes MMVC       | Seu diretório neste projeto |
|:---------------------------:|:---------------------------:|
|  Models (fontes de dados)   |           dados/            |
| domain (lógica de negócios) |          backend/           |
|  View (interface gráfica)   |           app_ui/           |


Além destes diretórios, há também um muito importante: **core/**. Nele está contido os
módulos, classes e funções para criação de menus, processamento de entrada do usuário e
manipulação da tela do terminal. É basicamente usado pelos arquivos Python dentro de
**app_ui/**.

**As subsessões a seguir a respeito dos componentes de arquitetura do projeto foram
inteiramente escritas pelo agente de IA assistente gemini-cli. Esses componentes incluem
"core/", "backend/", "dados/" e "app_ui/". Apesar disso, ainda é util para entender onde
encontrar o que. Obviamente, eu os revisei.**

## Core.
Como mencionado, o diretório **core/** funciona como o "motor" por trás da interface. Em
vez de espalhar lógicas de `input()` e `print()` por todo o código, concentrei aqui as
abstrações que lidam com a limpeza do terminal, validação de tipos de dados (garantindo que
o programa não quebre se o usuário digitar uma letra onde se espera um preço) e a
construção dinâmica dos menus. Isso permite que a interface seja alterada globalmente
apenas modificando estes arquivos.

## Backend.
Este é o "coração" do sistema, onde reside a lógica de negócios. O diretório **backend/** contém as entidades que definem o comportamento do carrinho:
*   **Produto**: Define as propriedades de cada item.
*   **Carrinho**: Gerencia a lógica de adição, remoção e cálculo de totais.
*   **Nota Fiscal**: Responsável por processar e formatar os dados para a saída final.
O importante aqui é que o backend é "cego" em relação à interface; ele apenas processa
dados e retorna resultados, o que facilita testes e futuras expansões.

## Dados.
Para que as informações não se percam cada vez que o programa é fechado, o diretório
**dados/** cuida da persistência. Ele utiliza um arquivo JSON como um banco de dados
simplificado. A classe de armazenamento aqui contida é responsável por traduzir os objetos
Python para o formato JSON e vice-versa, garantindo que o estado do sistema seja preservado
entre as execuções.

O arquivo json responsável pelo armazenamento (produtos.json) é vizinho do arquivo Python
responsável por gerenciá-lo, isto é, "armazenamento\_produtos.py".

## App UI
Finalmente, o diretório **app_ui/** é onde a interface ganha vida. Ele utiliza as
ferramentas do **core/** para apresentar a lógica do **backend/** ao usuário. Cada submenu
(como o de análise de gastos ou o de gerenciamento de itens) está isolado em seu próprio
módulo, tornando a navegação organizada e o código fácil de localizar. O arquivo `ui.py`
atua como o orquestrador principal, ligando todos esses componentes.

Cada menu presente no sistema foi posto na pasta "app\_ui/menus". Como dito,
"app\_ui/ui.py" é responsável por chamar todos os menus incluído nesta pasta.

# Usando as abstrações de menu.
As "abstrações de menu" incluem as classes para criação dos menus, controle de tela e 
processamento de entrada do usuário. A lista a seguir mostra quais classes são essas e
o que fazem.

- Menu: cuida do gerenciamento de um menu, o que inclui imprimir as opçoes de um menu e
  receber a entrada do usuário. Não implementa um loop.
- criar_menu: função que recebe um Menu e o mantém em um loop, além de desfazê-lo quando o
  usuário desejar.
- Option: Classe que associa uma função a uma opção de menu. a classe Menu aceita uma lista
  de opções. Também poderíamos usar dicionários para esse problema.
- ControloadorTela: com ela conseguimos limpar o terminal, exibir mensagens para o usuário
  e mostrar erros ao usuário.
- InteraçãoComUsuario: classe responsável por interagir com o usuário, obrigá-lo a inserir
  respostas formatadas (real para real, texto para texto, inteiro para inteiro, etc.) e
  realizar a converções de tipo automaticamente.

Para criar um menu, é necessário fornecer uma lista de objetos **Options**, que associam
um rótulo a uma função. Dessa maneira, **Menu** cuida para que a opção selecionada pelo
usuário acione a função relacionada. Essas funções também podem ser métodos de classe,
motivo pelo qual todos os menus do sistema foram feitos usando uma classe. Além
das opções, também é preciso fornecer o título que o menu exibirá no topo e uma função 
isolada, que será executada pelo Menu sempre que este for construído.

A seguir, um exemplo de um menu sendo criado **fora de uma classe**, seguido de um 
**dentro de uma classe**

``` python
from core/criar_menu import Menu, Option, InteracaoConUsuario, ControladorTela

def exibir_um():
	print(1)
def exibir_dois():
	print(2)
def sair():
	return controlador.SAIR
	
menu = Menu([
	Option("Exibir 1", exibir_um),
	Option("Exibir 2", exibir_dois)
])

criar_menu(menu)
```

Agora, um menu dentro de uma classe:

``` python
from core/criar_menu import Menu, Option, InteracaoConUsuario, ControladorTela
class MenuExibirNumeros:
	def __init__(self):
		self.__menu = menu = Menu([
			Option("Exibir 1", self.exibir_um),
			Option("Exibir 2", self.exibir_dois),
			Option("Sair", self.sair)
		])
	def exibir_um(self):
		print(1)
	def exibir_dois(self):
		print(2)
	def sair(self):
		return self.controlador.SAIR
	
```
