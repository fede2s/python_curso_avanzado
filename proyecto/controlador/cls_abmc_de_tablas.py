import flet
import datetime
from modelo.cls_db_sqlite3 import DbSqlite3
import vista.cls_vista_abmc_tabla as vista_tab
import modelo.cls_validador_clave as lib_regex_clave
from modelo.cls_log_excepciones import RegistroLogError
from decoradores.registrar_en_txt import registrar_en_txt


# controlador principal de la app
class ControladorDeTablas:
    """
    Tabla con datos:

    En el constructor del controlador, instancio una tabla de base de
    datos donde en su constructor:
        1) Primero verifico si existe la base y si no la creo
        2) Después verifico si la tabla está creada en la base de
           datos y si no la creo

    Después, en el método inicializar del controlador y llamando
    métodos de la vista y métodos de la tabla de la base de datos:
        1) Defino las funciones ABM y Alerta para manejar la lógica
           entre la vista y el modelo (tabla en base de datos)
        2) Consulto datos de la tabla a la base de datos
        3) Consulto los títulos de las columnas de la tabla en la base
           de datos
        4) Construyo la tabla en Flet asignándole los títulos a cada
           columna y los datos a cada fila
    """
    def __init__(
            self,
            page,
            nombre_base_de_datos="federico_dos_santos.db",
            nombre_tabla="agenda_de_guardias",
            campos_de_tabla=[
                "id INTEGER PRIMARY KEY AUTOINCREMENT",
                "fecha DATE NOT NULL",
                "hora_inicio TIME NOT NULL",
                "ID_EMPLEADO INTEGER NOT NULL",
                "ID_SUPLENTE INTEGER NOT NULL"]):
        self.tabla_bd = DbSqlite3(
            nombre_base_de_datos,
            nombre_tabla,
            campos_de_tabla
        )
        self.registro = []
        self.page = page
        self.separador = ''
        self.vista = \
            vista_tab.VistaABMCDeTablas(self.page, nombre_tabla)
        self.nombre_base_de_datos = nombre_base_de_datos
        self.nombre_tabla = nombre_tabla
        self.campos_de_tabla = campos_de_tabla
        self.vista.page.controls.clear()
        self.inicializar()
        self.log = 'log_errores.txt'

    def inicializar(self):
        def alta(e):
            datos = []
            # armo los datos a insertar en una lista
            for campo in self.vista.registro_modificable.controls:
                datos.append(campo.value)
            try:
                lib_regex_clave.ValidadorClave.validar_clave(datos[0])
            except RegistroLogError as log:
                print("Error al validar la clave")
                log.registrar_error()

            # llamo al metodo insertar datos en sqlite3
            try:
                self.tabla_bd.insertar_datos(datos)
                datos = self.tabla_bd.consultar_tabla()
                self.actualizar_vista()
                self.vista.alerta_evento.title = \
                    'Registro agregado a base de datos'
                alerta(e)
            except Exception as error:
                print(error)
                self.vista.alerta_evento.title = \
                    'No se pudo insertar el registro'
                alerta(e)

        @registrar_en_txt
        def alerta(e):
            e.control.page.overlay.append(self.vista.alerta_evento)
            self.vista.alerta_evento.open = True
            e.control.page.update()
            mensaje_txt = self.vista.alerta_evento.title
            datos_txt = ''
            for campo in self.vista.registro_modificable.controls:
                datos_txt += ';' + str(campo.value)
            datos_txt = datos_txt[1:]
            return mensaje_txt + '\t' + datos_txt + '\n'

        def baja(e):
            # selecciono la primera celda del registro
            id = self.vista.registro_modificable.controls[0].value

            # Verifico si es valida la clave
            try:
                lib_regex_clave.ValidadorClave.validar_clave(id)
            except RegistroLogError as log:
                print("Error al validar la clave")
                log.registrar_error()

            """
            verifico si existe, porque sino no lo puedo borrar
            y debo informarlo
            """
            registro = self.tabla_bd.consultar_tabla(id)
            if registro == []:
                self.vista.alerta_evento.title = \
                    f'No existe el registro {id}'\
                    + ', no se puede borrar'
                alerta(e)
                return

            try:
                self.tabla_bd.borrar_registro(id)
                self.actualizar_vista()
                self.vista.alerta_evento.title = \
                    f'Registro con id={id} eliminado'
            except Exception as error:
                self.vista.alerta_evento.title = \
                    f'Error al borrar el registro con id={id}'
                print(error)
            alerta(e)

        def modificacion(e):
            id = self.vista.registro_modificable.controls[0].value

            """
            Valido la clave
            """
            try:
                lib_regex_clave.ValidadorClave.validar_clave(id)
            except RegistroLogError as log:
                print("Error al validar la clave")
                log.registrar_error()

            """
            verifico si existe, porque sino no lo puedo modificar
            y debo informarlo
            """
            registro = self.tabla_bd.consultar_tabla(id)
            if registro == []:
                self.vista.alerta_evento.title = \
                    f'No existe el registro {id}'\
                    + ', no se puede modificar'
                alerta(e)
                return

            nuevos_datos_celdas = self.vista.registro_modificable.controls[1:]
            nuevos_datos = []
            for celda in nuevos_datos_celdas:
                print(celda.value)
                nuevos_datos.append(celda.value)
                print(nuevos_datos)

            try:
                self.tabla_bd.actualizar_registro(
                    id,
                    tuple(nuevos_datos))
                self.actualizar_vista()
                self.vista.alerta_evento.title = \
                    f'Registro con id={id} actualizado'
            except Exception as error:
                self.vista.alerta_evento.title = \
                    f'No se pudo actualizar el registro con id={id}'
                print(error)
            alerta(e)

        # Cargo una lista de tuplas con los datos de la consulta sql
        self.vista.datos = self.tabla_bd.consultar_tabla()
        # Cargo los titulos de las columnas
        self.vista.titulos_columnas = self.tabla_bd.obtener_columnas()
        self.vista.inicializar_vista(
            alta,
            baja,
            modificacion
        )

    def actualizar_vista(self):
        self.vista.datos = self.tabla_bd.consultar_tabla()
        self.vista.actualizar_tabla()
