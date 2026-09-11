import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Formulário"
    pagina.window.width = 320
    pagina.window.height = 600
    pagina.padding = 20

    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    caixatexto = ft.TextField(width = 280, content_padding = 10, label = 'Digite seu nome!', border_color = "#ddd", focused_border_color = ft.Colors.BLUE_200)

    checkbox = ft.Checkbox(label = "Aceito os Termos", value = False)

    mensagem = ft.Text("")

    def enviar(e):
        nome = caixatexto.value
        if nome == "" or checkbox.value == False:
            mensagem.value = "Preencha as informações e tente novamente."
        else:
            mensagem.value = f"Obrigado {caixatexto.value}!"
        

    pagina.add(
        ft.Container(
            width = 280,
            content = ft.Column(
                [
                    caixatexto,
                    checkbox,
                    ft.ElevatedButton(
                        content="Enviar", 
                        width=280,
                        height = 40,
                        style = ft.ButtonStyle(
                            shape = ft.RoundedRectangleBorder(
                                radius = 5
                            )
                        ),
                        on_click = enviar
                    ),
                    mensagem
                ]
            )
        )
    )

ft.run(main)