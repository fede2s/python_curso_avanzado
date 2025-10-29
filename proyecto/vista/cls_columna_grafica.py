from flet import Column


class ColumnaGrafica(Column):
    """ simplificado de ejemplo en
    https://flet.dev/docs/controls/column


    Clase que hereda de flet.Column.
    Su constructor recibe solamente objetos flet.
    """
    def __init__(self, objetos):
        super().__init__(expand=False, spacing=50, controls=objetos)
