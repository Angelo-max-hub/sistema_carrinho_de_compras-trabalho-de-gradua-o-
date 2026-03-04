"""
Ponto de entrada principal do sistema de carrinho de compras.

Este script é responsável por inicializar a aplicação e disparar
o menu principal da interface de usuário.
"""

from app_ui.ui import MenuPrincipal

# Usa a interface fornecida pelo arquivo app_ui/ui.py, que cria e gerencia
# os menus de terminal, com o qual o usuário interage com o carrinho.
# Veja mais sobre a arquitetura na sessão "Arquitetura do sistema", em
# README.md, na raiz do projeto.

app = MenuPrincipal()
app.iniciar_menu_principal()
