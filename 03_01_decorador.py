"""Ejemplo 1 usando funcion"""
def decorador_multiplicar_por_10(funcion):
    def envoltura(*args):
        print(funcion(*args)*10)
    return envoltura

@decorador_multiplicar_por_10
def sumar(a,b):
    c=a+b
    return c

sumar(2,3) # imprime 50 porque el decorador multiplica por 10


""" Ejemplo 2 usando clase """
class Operaciones:
    @decorador_multiplicar_por_10
    def sumar(self,a,b):
        c=a+b
        return c

obj = Operaciones()
obj.sumar(2,3)


"""
Cuando uso una clase decoradora, no puedo usarla
sobre métodos, solo puedo usarla sobre funciones.

Se implementa una clase constructora, que implementa
el método __call__ para poder atrapar la función con
sus parámetros. La desventaja es que no lo podemos usar
sobre métodos, solamente sobre funciones.
"""

class DecoradorMultiplicarPor10:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self,*args):
        print(self.func(*args)*10)

@DecoradorMultiplicarPor10
def sumar(a,b):
    c=a+b
    return c

sumar(2,3) # imprime 50 porque el decorador multiplica por 10

"""Decorador de clase
Hacemos una clase envoltura que va a tener un constructor __init__
Y va a tener un método __getattr__ que al llamarlo le agrega funcionalidad
a los atributos cada vez que sean llamados
"""

def decorador(cls):
    class Envoltura:
        def __init__(self,*args):
            self.instancia_de_clase = cls(*args)

        def __getattr__(self,nombre):
            print(self.__class__)
            print(self.instancia_de_clase.__class__)
            print("Nombre de atributos de la clase Auto: ", nombre)
            return getattr(self.instancia_de_clase, nombre)

    return Envoltura

@decorador
class Auto:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

x=Auto("Rojo","Renault")
print(x.color)
print(x.marca)


"""
Apilado de decoradores:
"""
def cambio_estado(f):
    def inner(*args, **kwargs):
        if args[0]:
            f(*args,**kwargs)
            print('El motor se ha encendido')
        else:
            f(*args,**kwargs)
            print('El motor se ha apagado')
    return inner

def aviso_cambio_estado(f):
    def inner(*args,**kwargs):
        print("Se envia un mensaje de celular")
        f(*args,**kwargs)
        print("Se ejecutó %s " % f.__name__)
    
    return inner

@cambio_estado
@aviso_cambio_estado
def estado_motor(estado):
    print(estado)

estado_motor(True)
print('*'*70)
estado_motor(False)

""" Parámetro dentro de decorador
Al llamarlo al decorador sobre la definicion de una funcion
tengo que pasarle un parametro al decorador

"""
def modo_de_trabajo (valor = False):
    def _modo_de_trabajo(funcion):
        def interna(*args, **kwargs):
            if valor:
                print('Estoy en produccion')
            else:
                print("Estoy en desarrollo")
            funcion(*args, **kwargs)
        return interna
    return _modo_de_trabajo

@modo_de_trabajo(False)
def registro_usuario(nombre, apellido):
    print('Registro de : %s ' %nombre)

registro_usuario('Fede', 'dos Santos')