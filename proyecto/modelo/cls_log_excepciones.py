import os
import datetime


class RegistroLogError(Exception):  # clase administradora
    """
    Registro de log, genera un txt con los errores.
    Voy una carpeta atras de donde estoy para que me
    salga junto con el main el log.txt
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, 'log_errores.txt')

    def __init__(self, linea, archivo, fecha):
        """ recibe id, archivo, fecha"""
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

    def registrar_error(self):
        log = open(self.ruta, "a")
        print(
            "Se ha dado un error:",
            self.archivo,
            self.linea,
            self.fecha,
            file=log
        )
        log.close()


"""Pruebas"""
if __name__ == "__main__":
    def registrar():
        # poner la fecha actual
        raise RegistroLogError(7, "archivo1.txt", datetime.datetime.now())
    try:
        registrar()
    except RegistroLogError as log:
        log.registrar_error()
