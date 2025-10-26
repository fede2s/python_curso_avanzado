"""
Delegacion, namespaces y sobrecarga de operadores, uso de slot

Delegacion
es como un contrato. en una clase padre, se define
un metodo y luego en una clase hija que hacen la
misma accion de diferentes formas. Delega que la clase
hija decida como llevar la accion adelante



"""
class Personas:
    def comer_arroz(self):
        self.accion()

class Chinos(Personas):
    def accion(self,):
        print('come arroz con palitos')

x = Chinos()
x.comer_arroz()

"""
Namespaces
una ruta indicada por el nombre de modulos.nombre_de_variable
Cuando genero una instancia tambien se genera un namespace,
un diccionario que tiene como clave los atributos de la instancia

si en el init defino algun atributo, me sale al ejecutar el 
método __dict__ dentro de un diccionario
"""

class ClasePadre():
    atributo='verde'
    def metodo_1(self,):
        pass

class ClaseHija(ClasePadre):
    atributo='verde'
    def metodo_1(self,):
        pass

class ClaseHija2(ClasePadre):

    def __init__(self, color):
        self.color = color
    atributo='verde'
    def metodo_1(self,):
        pass

x=ClaseHija()
y=ClaseHija2('verde')

print(x.__dict__) # no imprime nada porque no tiene atributos de instancia

print(y.__dict__) # imprime {'color': 'verde'}

# tupla con las clases de la que está heredando
print(ClaseHija.__bases__) # imprime (<class '__main__.ClasePadre'>,)

# la clase a la cual pertenece la instancia
print(x.__class__) # imprime <class '__main__.ClaseHija'>

# claves del diccionario asociado a la ClaseHija2
print(ClaseHija.__dict__.keys()) # imprime dict_keys(['__module__', 'atributo', 'metodo_1', '__doc__'])

"""
Sobrecarga de operadores
Son palabras reservadas o métodos reservados de python
que nos ayudan a atrapar la instancia de un determinado
objeto y hacer que se ejecute un método con una acción
determinada.
Son como métodos predefinidos por python que si decidimos
usarlos nos permiten atrapar la instancia y hacer algo
con esa instancia
"""

class Usuarios:
    def __init__(self,nombre):
        self.nombre = nombre

    """ cuando imprima el objeto en vez de imprimir que 
    es un objeto va a imprimir lo que retorna el metodo
    __str__()
    """
    def __str__(self,):
        return 'el nombre de usuario es:' + self.nombre

x = Usuarios('Anna')
print(x) # imprime el nombre de usuario es:Anna

class Indice:
    """
    Me permite asignarle un item y hacer algo con ese
    item
    """
    lista = ['m','a','n','z','a','n','a']
    def __getitem__(self, indice):
        return indice**0.5
    
    def __setitem__(self, indice, valor):
        self.lista[indice]=valor

x = Indice()
print(x[64]) #imprime 8
x[6]='o'
print(x.lista) #imprime ['m', 'a', 'n', 'z', 'a', 'n', 'o']


""" sobrecarga de operadores
algoritmo más complejo

iter actua junto con next
cuando calculo un iter de la instancia x comienza 
a tomar los valores y cada vez que pase al next 
toma el siguiente valor
 """
class RaizCuadrada:
    # toma una lista y la longitud
    def __init__(self,a):
        self.a=a
        self.n=len(self.a)

    # ordena la lista y llama una clase auxiliar
    def __iter__(self,):
        for i in range(self.n-1):
            for j in range(self.n-1):
                if(a[j]>a[j+1]):
                    aux=a[j]
                    a[j] = a[j+1]
                    a[j+1] = aux
        return RecorrerIteracion(self.a)

# toma los elemenos de la lista que ya estan
#  ordenados y realiza el calculo de raiz cuadrada del elemento que le sigue
class RecorrerIteracion():
    def __init__(self,a):
        self.a=a
        self.longitud = len(self.a)-1
        self.i=-1

    def __next__(self,):
        if self.i==self.longitud:
            raise StopIteration
        self.i+=1
        return self.a[self.i]**0.5

a=[81,16,64,9]
x=RaizCuadrada(a)
p=iter(x)
print(next(p),next(p),next(p)) #imprime 3.0 4.0 8.0

""" Slot
son una herramienta util para cuando tenemos poca memoria
y queremos limitar la cantidad de espacio que cada instancia
pueda ocupar en la memoria
Luego no puedo usar el método __dict__ porque no se guardan
en un diccionario los atributos
Para recuperar los atributos puedo implementar setattr y getattr
Además para agregar de forma dinámica nuevos atributos podemos
agregar a __slots__ el __dict__ en el último lugar
Ej:
class Limites:
    __slots__=['edad','sexo','trabajo','salario',__dict__']
"""

class Limites:
    __slots__=['edad','sexo','trabajo','salario']

x = Limites()
x.edad=4
print(x.edad) # imprime 4
# x.peso=10
# print(x.peso) # imprime AttributeError: 'Limites' object has no attribute 'peso'

setattr(x,'sexo','masculino')
print(getattr(x,'edad')) # imprime edad
print(getattr(x,'sexo')) # imprime masculino