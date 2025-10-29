import sqlite3


class DbSqlite3():
    """
    Clase con...

    Atributos de instancia
    ======================

    - **nombre_base**: nombre de la base de datos SQLite.
    - **nombre_tabla**: nombre de la tabla a utilizar.
    - **campos**: definición de las columnas de la tabla.

    Métodos de instancia privados
    =============================

    - **__crear_base(self)**: crea la base de datos si no existe.
    - **__crear_tabla(self)**: crea la tabla en la base de datos si no
      existe.

    Métodos públicos
    ================

    - **insertar_datos(self)**: inserta registros en la tabla.
    - **borrar_registro(self)**: elimina un registro de la tabla.
    - **actualizar_registro(self)**: actualiza un registro existente.
    - **consultar_tabla(self)**: consulta todos los registros de la
      tabla.
    - **listar_tablas(self)**: lista todas las tablas de la base de
      datos.
    - **obtener_columnas(self)**: obtiene los nombres de las columnas
      de la tabla.
    """
    def __init__(
            self,
            nombre_base,
            nombre_tabla,
            campos):
        """
        El constructor define los atributos de instancia y los carga
        Ademas ejecuta los metodos privados: crear_base() y
        crear_tabla()
        """
        self.nombre_base = nombre_base
        self.nombre_tabla = nombre_tabla
        self.campos = campos
        self.__crear_base()
        self.__crear_tabla()

    def __crear_base(self):
        con = sqlite3.connect(self.nombre_base)
        con.commit()
        con.close()

    def __crear_tabla(self):
        campos = ', '.join(self.campos)
        sql = "CREATE TABLE if not exists " \
            + f"{self.nombre_tabla} ({campos});"
        try:
            con = sqlite3.connect(self.nombre_base)
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            print(f"Tabla '{self.nombre_tabla}' "
                  + " creada exitosamente.")
            con.close()
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            con.close()

    def insertar_datos(self, datos):
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        if len(datos) == 0:
            print("No hay datos para insertar.")
            con.commit()
            con.close()
            return
        placeholders = ', '.join(['?'] * len(datos))
        print(datos)
        print(placeholders)
        sql = f"INSERT INTO {self.nombre_tabla} " \
            f"VALUES ({placeholders})"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def borrar_registro(self, id):
        sql = f"DELETE FROM {self.nombre_tabla} WHERE id = ?"
        data = (id,)
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        con.close()

    def actualizar_registro(
            self,
            id,
            nuevos_datos):
        sql = f"UPDATE {self.nombre_tabla} SET "
        nombres_columnas = self.obtener_columnas()
        campos = nombres_columnas[1:]
        nombreid = nombres_columnas[0]
        for campo in campos:
            sql += f"{campo} = ?, "
        sql = sql[:-2]  # Elimino la última coma y espacio
        sql += " WHERE id = ?"
        data = tuple(nuevos_datos + (id,))
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        con.close()

    def consultar_tabla(self, id=None):
        if id is None:
            print("No se especificó un ID para consultar.")
            try:
                con = sqlite3.connect(self.nombre_base)
                cursor = con.cursor()
                sql = f"SELECT * FROM {self.nombre_tabla};"
                cursor.execute(sql)
                registros = cursor.fetchall()
                for registro in registros:
                    print(f"Registro leido: {registro}")
                con.commit()
                con.close()
                return registros
            except Exception as e:
                print(f"Error al consultar la tabla: {e}")
                con.commit()
                con.close()
                return None
        else:
            try:
                con = sqlite3.connect(self.nombre_base)
                cursor = con.cursor()
                sql = f"SELECT * FROM {self.nombre_tabla} WHERE id = ?;"
                data = (id,)
                cursor.execute(sql, data)
                registros = cursor.fetchall()
                for registro in registros:
                    print(f"Registro leido: {registro}")
                con.commit()
                con.close()
                return registros
            except Exception as e:
                print(f"Error al consultar la tabla: {e}")
                con.commit()
                con.close()
                return []

    def obtener_columnas(self):
        try:
            con = sqlite3.connect(self.nombre_base)
            cursor = con.cursor()
            cursor.execute(f"PRAGMA table_info({self.nombre_tabla});")
            columnas = cursor.fetchall()
            # Extraer solo los nombres de las columnas
            nombres_columnas = [columna[1] for columna in columnas]
            con.commit()
            con.close()
            return nombres_columnas
        except Exception as e:
            print("Error al obtener las columnas de la tabla "
                  + f"'{self.nombre_tabla}': {e}")
            con.commit()
            con.close()
            return []

    def listar_tablas(self):
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(sql)
        tablas = cursor.fetchall()
        for tabla in tablas:
            print(f"Tabla: {tabla[0]}")
        con.commit()
        con.close()
        return tablas
