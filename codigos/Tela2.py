import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Informações Perfil"
    pagina.bgcolor = "#CDCACA"
    pagina.window.width = 320
    pagina.window.height = 600
    pagina.padding = 20

    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nome = ft.Text(
        "Caio Yuri",
        size=25,
        color="#00d5ff"
    )

    subtitulo = ft.Text(
        "Bem Vindo ao nosso APP",
        size=15,
        color="#00d5ff"
    )

    email = ft.Text(
        "caio@gmail.com",
        size=15,
        color="#00d5ff"
    )   

    telefone = ft.Text(
        "Telefone: (11) 99999-9999",
        size=15,
        color="#00d5ff"
    )         

    pagina.add(
        ft.Container(
            width=380,
            content=ft.Column(
                [
                    nome,
                    subtitulo,

                    ft.Row(
                        [
                            ft.Icon(ft.Icons.EMAIL, color="#00d5ff"),
                            email
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    ft.Row(
                        [
                            ft.Icon(ft.Icons.PHONE, color="#00d5ff"),
                            telefone
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="#0F0063",
            padding=20,
            border_radius=10
        )
    )

ft.run(main)