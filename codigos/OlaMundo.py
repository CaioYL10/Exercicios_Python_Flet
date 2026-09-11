import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Plant 🪻"
    pagina.add(ft.Text('Olá পরিবাহী!'))

ft.run(main)

# ft.run(main, view=ft.AppView.WEB_BROWSER) Para abrir Web