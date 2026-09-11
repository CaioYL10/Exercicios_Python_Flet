import flet as ft

def main(page: ft.Page):
    page.title = "Meu App"
    page.bgcolor = "#19DCFF"
    page.window.width = 320
    page.window.height = 600
    page.padding = 20

    titulo = ft.Text(
        "CaioY Corp",
        size=35,
        color="white"
    )

    subtitulo = ft.Text(
        "Bem-vindo ao nosso aplicativo!",
        size=20,
        color="white"
    )

    page.add(
    ft.Column(
        [
            titulo,
            subtitulo
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
)

ft.run(main)