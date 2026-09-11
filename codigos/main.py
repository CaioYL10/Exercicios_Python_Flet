import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criando Funções
    def diminuir (e):
        caixa_texto.value = str(int(caixa_texto.value) - 1)

    def aumentar (e):
        caixa_texto.value = str(int(caixa_texto.value) + 1)

    # Criando os itens da página 
    botao_menos = ft.IconButton(ft.Icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLUE)
    botao_mais = ft.IconButton(ft.Icons.ADD, on_click=aumentar)

    # Adicionando na página
    page.add(ft.Row([
            botao_menos, 
            caixa_texto, 
            botao_mais,
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ))

ft.run(main, view=ft.AppView.WEB_BROWSER)

