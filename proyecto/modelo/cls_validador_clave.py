import datetime
from re import compile
from modelo.cls_log_excepciones import RegistroLogError


class ValidadorClave():
    """Clase que sirve para validar claves"""
    @staticmethod
    def validar_clave(clave):
        """
        las claves deben ser patron numerico
        Al menos 1 numero
        Menos de 10 numeros porque el integer de SQL llega a 2.147.483.647
        """
        patron = compile('[0-9]{1,10}')
        if patron.match(clave):
            return True
        else:
            raise RegistroLogError(
                f"ID ingresado: {clave}\t",
                "Archivo: regex_validar_clave.py\t",
                f"timestamp {datetime.datetime.now()}"
            )
