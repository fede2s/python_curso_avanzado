import flet as ft
import vista.cls_boton
import vista.cls_fila_grafica
import vista.cls_columna_grafica
import vista.cls_generador_obj_flet as obj_flet


class VistaABMCDeTablas():
    """
    Atributos de instancia
    ======================

    - **page**: página de Flet.
    - **titulos_columnas**: muestra qué representa cada columna.
    - **datos**: contiene la información a graficar en una tabla de
      Flet.
    - **botones**: fila de botones de Flet con funciones **ABM** que
      provienen del controlador (y este a su vez del modelo).
    - **registro_modificable**: utilizado para funciones de **ABM**.
    - **tabla**: la tabla a graficar con Flet y con los datos que
      provee el controlador.
    - **separador**: separa la parte superior (botones y registro
      modificable) de la parte inferior (tabla).
    - **alerta_evento**: alerta cuando se ejecuta una función **ABM** o
      cuando ocurre un error.

    Métodos de instancia públicos
    =============================

    - **actualizar_tabla(self)**: actualiza los datos de la tabla.
    - **inicializar_vista(self, alta, baja, modificacion)**: inicializa
      la vista asignando las funciones de **ABM**.

    Métodos de instancia privados
    =============================

    - **__inicializar_botones(self)**: inicializa los botones de la
      vista.
    - **__inicializar_registro_modificable(self)**: inicializa el
      registro modificable.
    - **__inicializar_tabla(self)**: inicializa la tabla de la vista.
    """
    def __init__(self, page, nombre_tabla):
        # configuración
        self.page = page
        self.page.title = f"ABMC de tabla {nombre_tabla}"
        self.page.scroll = "always"
        self.page.update()

        # para funcionamiento
        self.titulos_columnas = []
        self.datos = []

        # Objetos visibles
        self.botones = None
        self.registro_modificable = None
        self.tabla = None
        self.separador = None
        self.alerta_evento = ft.AlertDialog(
            title=ft.Text('')
        )

    def __inicializar_tabla(self):
        """
        genero una tabla de forma dinamica con la tabla que estoy
        consultando y con la vista que tengo para tablas
        """
        self.tabla = obj_flet.GeneradorObjetosFlet.generar_tabla(
            columnas_txt=self.titulos_columnas,
            filas_lista_txt=self.datos
        )

    def actualizar_tabla(self):
        """Actualiza los datos en la tabla"""
        self.tabla.rows.clear()
        self.tabla.rows = \
            obj_flet.GeneradorObjetosFlet.generar_filas_de_tabla(self.datos)
        self.page.update()

    def __inicializar_botones(
            self,
            funcion_alta,
            funcion_baja,
            funcion_modificacion):
        """
        Botones: primero creo boton alta, baja, modificacion
        Después los junto en una fila usando la funcion generar filas
        y pasandole una lista de los botones
        """
        boton_alta = vista.cls_boton.Boton("Alta", funcion_alta)
        boton_baja = vista.cls_boton.Boton("Baja", funcion_baja)
        boton_modificacion = vista.cls_boton.Boton(
            "Modificacion",
            funcion_modificacion)

        self.botones = vista.cls_fila_grafica.FilaGrafica(
            [boton_alta, boton_baja, boton_modificacion]
        )

    def __inicializar_registro_modificable(self):
        """
        Celdas modificables / Registro modificable:
        Agrego elementos a la lista REGISTRO que a la vez es
        un atributo de la clase abmc_de_tablas. Ese nuevo
        elemento es un elemento de Flet de tipo TextField
        """
        registro_modificable = []
        for campo in self.titulos_columnas:
            registro_modificable.append(
                ft.TextField(
                    value='',
                    label=campo,
                    width=150))
        lista_celdas_modificables = []
        for campo in self.titulos_columnas:
            lista_celdas_modificables.append(
                ft.DataCell(content=ft.Text(campo),)
                )
        self.registro_modificable = \
            vista.cls_fila_grafica.FilaGrafica(registro_modificable)

    def inicializar_vista(
            self,
            alta,
            baja,
            modificacion):
        """
        Inicializo los distintos objetos flet que componen la vista
        """
        self.__inicializar_botones(alta, baja, modificacion)
        self.__inicializar_registro_modificable()
        self.__inicializar_tabla()
        """
        Formulario:
        es una columnas donde 1era fila va la fila de botones
        en segunda fila va una fila de celdas modificables
        """
        formulario = vista.cls_columna_grafica.ColumnaGrafica([
            self.botones,
            self.registro_modificable
        ])

        """
        Genero un separador que separa con una línea móvil al
        formulario de la tabla.
        Finalmente el formulario que contiene todos los objetos
        a la página.
        """
        self.separador = obj_flet.GeneradorObjetosFlet.generar_separador(
            formulario,
            self.tabla
            )
        self.page.add(self.separador)
