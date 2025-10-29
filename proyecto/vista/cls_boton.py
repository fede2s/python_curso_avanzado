from flet import OutlinedButton


class Boton(OutlinedButton):
    """Clase que hereda de flet.OutlinedButton, pero simplifica
    los atributos que recibe el constructor en: texto, funcion
    """
    def __init__(self, texto, funcion):
        super().__init__()
        self.text = texto
        self.on_click = funcion
