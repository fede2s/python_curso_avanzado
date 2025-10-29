"""
Patrones que vimos: MVC, Delegacion, Iterador

Patrones que veremos: Observador, Adaptador, Factory, Singleton

Patron Observador: tenemos un tema que podría ser la clase abmc o
por ejemplo un alta de registro, cuando por ejemplo un objeto de la
clase abmc de registro hace algo quiero que el observador informe
---------------------------------------------------------------------
El sujeto u observador debe heredarle a abmc
o sea en modelo.py hago un:
    from observador import sujeto

Además el observador.py tiene la clase sujeto igual que acá pero con
un parametro *args en el método notificar para pasarle a update(args)

Luego en modelo.py la clase Abmc hereda de Sujeto
---------------------------------------------------------------------
el observador concreto debe estar instanciado como atributo del
controlador y le paso vista.objeto_abmc ( o sea en realidad le paso
el abmc lo que pasa es que el profe lo tiene en la vista en vez de
en el controlador)

entonces en controler.py
    import observador

class Controller:
    def __init__(self,root):
    self.el_observador = observador.ConcreteObserverA(self.objeto_vista.objeto_base)

donde objeto_base es una instancia de la clase Abmc
---------------------------------------------------------------------
"""

class Subject:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        for observador in self.observadores:
            observador.update()

class TemaConcreto(Subject):
    def __init__(self,):
        self.estado = None

    def set_estado(self,value):
        self.estado = value
        self.notificar()

    def get_estado(self,):
        return self.estado
    
class Observador:
    def update(self,):
        raise NotImplementedError("Delegación de actualización")

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self,):
        print('Actualización dentro de Observador ConcreteObserverA')
        self.estado = self.observado_a.get_estado()
        print('Estado ' , self.estado)

tema1 = TemaConcreto()
observador_a = ConcreteObserverA(tema1)
tema1.set_estado(1)