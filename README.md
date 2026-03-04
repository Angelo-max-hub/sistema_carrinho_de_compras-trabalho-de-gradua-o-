# Introdução.
O programa contido neste repositório é a solução para um trabalho de graduação no curso
Tecnólogo em Análise e Desenvolvimento de Sistemas. Consiste em criar um programa em Python
simples que simula um sistema de carrinho, com o qual o usuário pode adicionar produtos e
realizar tarefas relacionadas a um sistema deste tipo, como calcular total de custo ou
imprimir nota fiscal.  Este trabalho foi pensado para fixação de conceitos de orientação a
objetos na disciplina "Linguagem de Programação II".

Apenas uma pequena parte deste documento fala sobre instalação e execução do programa, que
é a sessão a seguir. O restante apresenta muito sobre detalhes internos e decisões sobre a
implementação, então sugiro que as ignore se apenas deseja executar o projeto na própria
máquina.

As classes principais do trabalho estão no diretório **"backend/"**, isto é, **Produto**,
**Carrinho** e **NotaFiscal**.

A seguir, mais sobre a implementação, arquitetura, instalação e uso do sistema, que, aliás,
não possui interface gráfica.

## Como instalar e usar.
A instalação é a maneira padrão de realizar isso no git hub: através de um pull ou
instalando o arquivo ZIP pelo site do GitHub, onde está hospedado este projeto.

Quanto ao uso e execução do projeto, é necessário executar o arquivo principal do projeto:
**main.py**, que está no diretório raiz. É absolutamente necessário executar este arquivo
na raiz do projeto, pois os caminhos usados em todos os arquivos Python são relativos a
essa raiz. Então, executá-lo fora do projeto ou dentro de alguma subpasta possivelmente
resultará em erro.

![executando_projeto_no_terminal](/imagens/executando_projeto.png "Executando projeto no
terminal")
# Visão geral do sistema.
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

Decidi que isso era deselegante e não escalável, e por isso criei abstrações que tornavam a
criação de menus, opções, entradas de usuário e controle da tela automáticas e mais fáceis,
embora *um pouco imperfeitas*, pois ainda precisam de alguma refatoração. A seguir um
exemplo real da criação de um menu perfeitamente funcional utilizando as abstrações que
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

Com esse sistema o usuário é capaz de adicionar ou remover produtos, calcular desconto ou
custo total e gerar notas fiscais. Além disso, **é capaz de se lembrar das informações que
o usuário adiciona**. Essas informações apenas podem ser os nomes e os preços dos produtos
incluídos. Portanto, os produtos não somem entre as execuções. E isso é possível graças ao
arquivo json e código Python contido em "dados/"

# Um pouco sobre a arquitetura.

A organização de pastas deste projeto foi um pouco inspirada no padrão **MMVC**, isto é, há
uma divisão do sistema entre **Dados**, **Lógica de negócios** e **Interface gráfica**.
Esses componentes possuem cada um diretório neste sistema, dessa maneira:

|      Componentes MMVC | Seu diretório neste projeto |
|:---------------------------:|:---------------------------:|
|  Models (fontes de dados) | dados/ |
| domain (lógica de negócios) | backend/ |
|  View (interface gráfica) | app_ui/ |


Além destes diretórios, há também um muito importante: **core/**. Nele está contido os
módulos, classes e funções para criação de menus, processamento de entrada do usuário e
manipulação da tela do terminal. É basicamente usado pelos arquivos Python dentro de
**app_ui/**.

O programa segue uma regra quanto a chamada de funções e classes: apenas "app_ui/" pode
usar "backend/", e apenas "backend/" pode usar "dados/". Isso também segue os princípios da
arquitura MMVC, e faz com que o sistema tenha um único sentido de comunicação.

Por fim, o arquivo "main.py", que deve ser o executado, tão somente utiliza o módulo
"app\_ui/ui.py", que é responsável por interagir com o usuário e utilizar os módulos em
"backend/"

## Core.
Como mencionado, o diretório **core/** funciona como o "motor" por trás da interface. Em
vez de espalhar lógicas de `input()` e `print()` por todo o código, concentrei aqui as
abstrações que lidam com a limpeza do terminal, validação de tipos de dados (garantindo que
o programa não quebre se o usuário digitar uma letra onde se espera um preço) e a
construção dinâmica dos menus. Isso permite que a interface seja alterada globalmente
apenas modificando estes arquivos.

## Backend.
Este é o "coração" do sistema, onde reside a lógica de negócios. O diretório **backend/**
contém as entidades que definem o comportamento do carrinho:
*   **Produto**: Define as propriedades de cada item.
*   **Carrinho**: Gerencia a lógica de adição, remoção e cálculo de totais.
*   **Nota Fiscal**: Responsável por processar e formatar os dados para a saída final.  O
importante aqui é que o backend é "cego" em relação à interface; ele apenas processa dados
e retorna resultados.

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
(como o de análise de gastos ou o de gerenciamento de carrinho) está isolado em seu próprio
módulo, tornando a navegação organizada e o código fácil de localizar. O arquivo `ui.py`
atua como o orquestrador principal, ligando todos esses componentes.

Cada menu presente no sistema foi posto na pasta "app\_ui/menus/". Como dito,
"app\_ui/ui.py" é responsável por chamar todos os menus incluído nesta pasta.

# Usando as abstrações de menu.
*Como as abstrações são como uma biblioteca simples, essa sessão serve como uma também
simples documentação. Por isso, se quiser ver mais informações sobre o projeto/trabalho,
sugiro que pule todas as subseções desta sessão.*

## Visão geral das abstrações de menu.
As "abstrações de menu" incluem as classes para criação dos menus, controle de tela e
processamento de entrada do usuário. A lista a seguir mostra quais classes são essas e o
que fazem.

- **Menu**: cuida do gerenciamento de um menu, o que inclui imprimir as opções de um menu e
  receber a entrada do usuário. Não implementa um loop.
- **criar_menu**: função que recebe um Menu e o mantém em um loop, além de desfazê-lo
  quando o usuário desejar.
- **Option**: Classe que associa uma função a uma opção de menu. A classe Menu aceita uma
  lista de objetos **Options**. Também poderíamos usar dicionários para esse problema.
- **ControloadorTela**: com ela conseguimos limpar o terminal, exibir mensagens para o
  usuário e mostrar erros ao usuário.
- **InteraçãoComUsuario**: classe responsável por interagir com o usuário, obrigá-lo a
  inserir respostas formatadas (real para real, texto para texto, inteiro para inteiro,
  etc.) e realizar a conversões de tipo automaticamente.

Para criar um menu, é necessário fornecer uma lista de objetos **Options**, que associam um
rótulo a uma função. Dessa maneira, **Menu** cuida para que a opção selecionada pelo
usuário acione a função relacionada. Essas funções também podem ser métodos de classe,
motivo pelo qual todos os menus do sistema foram feitos usando uma classe. Além das opções,
também é preciso fornecer o título que o menu exibirá no topo e uma função isolada, que
será executada pelo Menu sempre que este for construído. Há exemplos disso logo abaixo.

## Como criar uma opção para sair ou desfazer o menu.
Todo menu precisa de uma opção **sair**, com o qual o menu é desfeito. A classe "Menu" não
adiciona ela automaticamente: o desenvolvedor deve fazer isso. Para isso, é necessário
fazer com que a função associada com a opção "Sair do menu" retorne uma string "SAIR",
exatamente dessa maneira. Da seguinte maneira:

``` python
def sair():
	return "SAIR"
	
menu = Menu(
	Option("Sair", sair),
	titulo_menu="Selecione para sair."
)

criar_menu(menu)
```

Isso irá desenhar na tela, mais ou menos, o seguinte:

```
Selecione para sair.

1 - Sair.

<Insira aqui> 
```

Isso é possível porque a função "criar_menu" espera que alguma das opções do objeto Menu
fornecido retorne esta constante. O objeto "Menu", por sua vez, informa **criar_menu** de
qualquer retorno de função.

Embora o código acima funcione, eu criei uma constante com o valor "SAIR" para isso. Ela
está contida na classe "ControladorTela", de maneira que as opções para "sair" ou "voltar"
são feitas normalmente da seguinte forma:

``` python
def sair():
	# É possível usar instanciando ControladorTela na hora ou aproveitando uma instância
	# já existente.
	
	return ControladorTela().SAIR
	
	menu = Menu([
		Option("Sair", sair)
	],
		titulo_menu="Saia do menu"
		)
```

## Usando "ControladorTela" e "InteraçãoComUsuario".
As opções de menu, que **Option** associa a uma função, podem fazer "coisas" usando essas
duas classes: ControladorTela para manipular o terminal e InteraçãoComUsuario para se
comunicar com o usuário de maneira fácil e padronizada. Para usá-las, é necessário as
instanciar e depois utilizar seus métodos e seus atributos dentro das funções associadas a
opções de menu.

## Métodos e atributos importantes de ControladorTela.
A lista abaixo mostra os métodos e atributos públicos da classe ControladorTela e os
descreve:
- **SAIR**: Atributo que contém a string "SAIR", usada para sinalizar o encerramento de um
  menu.
- **limpar_tela()**: Limpa o terminal de forma multiplataforma (Windows e Linux/macOS).
- **esperar_enter()**: Pausa a execução do programa e aguarda o usuário pressionar a tecla
  \<ENTER\>.
- **esperar(espera: int)**: Pausa a execução por um número determinado de segundos.
- **imprimir_com_bordas(borda: str, mensagem: str)**: Imprime uma mensagem cercada por
  bordas personalizadas no terminal.
- **exibir_mensagem_de_erro(mensagem: str)**: Exibe uma janela de erro visualmente
  destacada no terminal.

## Métodos e atributos importantes de InteracaoComUsuario.
A lista abaixo mostra os métodos e atributos públicos da classe InteraçãoComUsuario:
- **imprimir_cabecario(titulo: str)**: Imprime um cabeçalho padronizado com o título
  fornecido.
- **obter_real(requisicao: str)**: Solicita e valida um valor real no formato brasileiro
  (ex: 2,99), retornando um `float`.
- **obter_inteiro(requisicao: str)**: Solicita e valida a entrada de um número inteiro,
  retornando um `int`.
- **obter_texto(requisicao: str)**: Solicita e valida a entrada de texto (apenas letras),
  retornando uma `str`.
- **formatar_numero_como_real(numero: float)**: Converte um `float` para uma string
  formatada como real brasileiro (ex: 12,99).


ControladorTela e InteraçãoComUsuario estão dentro de arquivos com o mesmo nome contidos na
pasta "core/", que estão documentados.

## O que e como importar as abstrações.
Tudo da pequena biblioteca criada, o que inclui funções, classes e constantes, deve ser
importadas do arquivo "core/criar_menu". Por exemplo:

``` python
from core.criar_menu import Menu, Option, ControladorTela, InteraçãoComUsuario
```

## Exemplos de uso.
A seguir, um exemplo de um menu sendo criado **fora de uma classe**, seguido de um **dentro
de uma classe**

``` python
from core/criar_menu import Menu, Option, InteracaoComUsuario, ControladorTela

def exibir_um():
	print(1)
def exibir_dois():
	print(2)
def sair():
	return controlador.SAIR
	
menu = Menu([
	Option("Exibir 1", exibir_um),
	Option("Exibir 2", exibir_dois)
],
	titulo_menu="Menu para números",
	funcao_inicial=None
	)

criar_menu(menu)
```

Agora, um menu dentro de uma classe:

``` python
from core/criar_menu import Menu, Option, InteracaoComUsuario, ControladorTela
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

## Opções que abrem menus.
O que pode parecer confuso sobre o sistema é que os menus existentes neles abrem menus
filhos, isto é, as opções que o usuário seleciona também podem abrir menus. Isso acontece
porque, quando associamos uma função a uma opção utilizando a classe **Option**, é
completamente possível que esta função utilize objetos Menu, Option, ControladorTela e
demais abstrações para gerar por si mesmo outro menu. Porém, embora isso seja possível, fiz
isso de uma maneira um pouco diferente.

O que fiz foi criar uma classe para cada menu inferior, e inseri seus métodos para desenhar
opções em um menu superior. O exemplo abaixo mostra um pouco sobre isso:

``` python
from core.criar_menu import Menu, Option, ControladorTela

# Classe que constrói o menu.
# __init__ configura o menu e "iniciar_menu" o  executa.
class MenuExibirNumero:
	def __init__(self):
		self.__menu = Menu([
			Option("Exibir 1", self.exibir_1),
			Option("Exibir 2", self.exibir_2)
		], 
			titulo_menu="Ver números"
		)
	def iniciar_menu(self):
		criar_menu(self.__menu)
		
	def exibir_1(self):
		print(1)
	
	def exibir_2(self):
   		print(2)

# Menu em si.
menu = Menu([
	Option("Abrir menu de números", MenuExibirNumero().iniciar_menu)
])
```

