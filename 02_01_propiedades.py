"""
podemos agregar logica extra
cuando: llamamos a un objeto, lo modificamos, eliminamos
cada vez que llame al usuario estoy llamando a la propiedad
que me permite agregar una lógica extra adentro
"""

class Cliente:

    def __init__(self,usuario):
        self._usuario=usuario
    def get_usuario(self,):
        print('Lógica de recuperar al usuario')
        return self._usuario
    def set_usuario(self,valor):
        print('Lógica para setear/modificar usuario')
        self._usuario = valor
    def del_usuario(self,):
        print('remover usuario')
        del self._usuario
    usuario = property(get_usuario, set_usuario, del_usuario, 'Descripcion de propiedad usuario')

cliente1=Cliente('Fede')
print(cliente1.usuario)
cliente1.usuario= 'Fede el más lindo'
print(cliente1.usuario)
del cliente1.usuario
print(Cliente.usuario.__doc__)

"""
Si tengo una clase padre empresa y una hija cliente
si la clase padre tiene una propiedad, la clase hija hereda"""
