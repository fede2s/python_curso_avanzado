import flet as ft


class GeneradorObjetosFlet():
    """Clase para generar objetos flet. Anteriormente tenia funciones.
    Ahora tengo metodos estaticos pertenecientes a esta clase"""

    @staticmethod
    def generar_filas_de_tabla(datos):
        filas = []
        for dato in datos:
            celdas = []
            for campo in dato:
                celdas.append(ft.DataCell(ft.Text(campo)))
            filas.append(ft.DataRow(celdas))

        return filas

    @staticmethod
    def generar_separador(
            botones,
            tabla):
        """
        copiado de repositorio oficial de flet
        https://github.com/flet-dev/examples/blob/main/python/apps/
        controls-gallery/examples/layout/divider/02_draggable_divider.py
        """
        def move_divider(e: ft.DragUpdateEvent):
            if (
                    (e.delta_y > 0 and c.height < 300) or
                    (e.delta_y < 0 and c.height > 100)):
                c.height += e.delta_y
            c.update()

        def show_draggable_cursor(e: ft.HoverEvent):
            e.control.mouse_cursor = ft.MouseCursor.RESIZE_UP_DOWN
            e.control.update()

        c = ft.Container(
            alignment=ft.alignment.center,
            height=150,
            content=botones
        )

        return ft.Column(
            [
                c,
                ft.GestureDetector(
                    content=ft.Divider(),
                    on_pan_update=move_divider,
                    on_hover=show_draggable_cursor,
                ),
                ft.Container(
                    alignment=ft.alignment.center_left,
                    expand=1,
                    content=tabla
                ),
            ],
            spacing=0,
            scroll=True
        )

    @staticmethod
    def generar_tabla(columnas_txt, filas_lista_txt):
        """
        copiado de repositorio oficial de flet
        https://github.com/flet-dev/examples/blob/main/python/apps/
        controls-gallery/examples/layout/datatable/01_basic_datatable.py
        lo hice dinamico para que reciba una lista de titulos de
        columnas y una lista de filas, donde cada fila es una lista
        de celdas
        """
        columnas = []
        filas = []
        for columna in columnas_txt:
            columnas.append(ft.DataColumn(ft.Text(columna)))
        for fila in filas_lista_txt:
            celdas = []
            for celda in fila:
                celdas.append(ft.DataCell(ft.Text(celda)))
            filas.append(ft.DataRow(cells=celdas))
        return ft.DataTable(
                columns=columnas,
                rows=filas
            )

    @staticmethod
    def generar_alerta(texto):
        """ copié código del repositorio oficial de flet
        https://github.com/flet-dev/examples/blob/main/python/apps/
        controls-gallery/examples/dialogs/alertdialog/01_basic_and_
        modal_dialogs.py
        """
        dlg = ft.AlertDialog(
            title=ft.Text(texto),
            on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def open_dlg(e):
            e.control.page.overlay.append(dlg)
            dlg.open = True
            e.control.page.update()

        return ft.Column(
            [
                ft.ElevatedButton(texto, on_click=open_dlg)
            ]
        )
