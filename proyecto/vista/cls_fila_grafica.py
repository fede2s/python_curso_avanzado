from flet import Row


class FilaGrafica(Row):
    """
    Encontré como generar una fila de contenedores acá
    https://flet.dev/docs/controls/container/


    Clase que hereda de flet.Row y su constructor recibe
    objetos de flet.


    **Es una fila grafica, no es fila de tabla.**
    """
    def __init__(self, objetos):
        super().__init__(objetos)
