"""
Este módulo contiene el punto de entrada de la aplicación Flet.

En :func:`main` se instancia un objeto de la clase
:class:`controlador.cls_abmc_de_tablas.ControladorDeTablas`, que funciona como
controlador para interactuar con el objeto de vista de la clase
:class:`vista.cls_vista_abmc_tabla.VistaABMCDeTablas` e interactua con los
distintos objetos instanciados de clases del modelo.
"""
import flet
import controlador.cls_abmc_de_tablas as abmc


def main(page: flet.Page):
    """
    Inicializa la aplicación Flet.

    Se crea una instancia de
    :class:`controlador.cls_abmc_de_tablas.ControladorDeTablas`
    y se le pasa la página Flet que se desea renderizar.
    """
    controlador = abmc.ControladorDeTablas(page)
    print(page)


flet.app(target=main)
