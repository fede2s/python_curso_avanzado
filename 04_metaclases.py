"""Para extender una clase, o sea, agregar un nuevo método
solo tengo que poner
MiClase.nuevo_metodo = funcion_definida_previamente

Podemos declarar clases con type(clase, herencia, {atributos y metodos})

Orden de ejecucion:
type -> new -> init -> metaclase ->new -> init -> clase -> new -> init-> decoradores

metaclase: hereda de type
Ej:
    class MetaClase(type):

"""
