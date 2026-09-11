import flet as ft

def main(page: ft.Page):
    page.title = "To Do List em Flet"
    page.window.width = 400
    page.window.height = 600
    page.padding = 20

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    caixatexto = ft.TextField(width = 200, content_padding = 10, label = 'Digite o produto!', border_color = "#ddd", focused_border_color = ft.Colors.BLUE_200)

    lista = ft.Column()

    def criarnovo(item):
        def diminuir(e):
            valor = int(contador.value)

            if valor > 0:
                contador.value = str(valor - 1)

        def aumentar(e):
            contador.value = str(int(contador.value) + 1)

        def deletar(e):
            lista.controls.remove(linha)

        
        contador = ft.TextField(value='0', width=50, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLUE)
        botao_menos = ft.IconButton(ft.Icons.REMOVE, on_click=diminuir)
        botao_mais = ft.IconButton(ft.Icons.ADD, on_click=aumentar)
        botao_remover = ft.IconButton(ft.Icons.DELETE, on_click=deletar)


        linha = ft.Row(
            controls = [
                ft.Text(item, width=120),

                botao_menos,
                contador,
                botao_mais,
                botao_remover
            ]
        )

        return linha

    def adicionar(e):
        if caixatexto.value:

            novo_item = criarnovo(caixatexto.value)

            lista.controls.append(novo_item)

            caixatexto.value = ""


    page.add(
        ft.Container(
            width = 320,
            content = ft.Column(
                [
                    ft.Row(
                        controls = [
                            caixatexto,
                            ft.Button(
                                content="Adicionar", 
                                width=120,
                                height = 40,
                                style = ft.ButtonStyle(
                                    shape = ft.RoundedRectangleBorder(
                                        radius = 5
                                    )
                                ),
                                on_click = adicionar
                            ),    
                        ]
                    ),

                    lista
                ]
            )
        )
    )

ft.run(main)