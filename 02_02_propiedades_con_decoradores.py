"""
Hace lo mismo que las propiedades, pero en vez
de usar property() uso los decoradores:
    @property
    @atributo.setter
    @atributo.deleter
"""
class Empresa:
    def __init__(self,usuario):
        self._usuario=usuario
    
    @property
    def usuario(self,):
        """Descripcion de usuario"""
        print('recuperar usuario')
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        print('Modificar usuario')
        self._usuario=valor

    @usuario.deleter
    def usuario(self,):
        print('Remover el usuario')
        del self._usuario

class Cliente(Empresa): pass

x = Cliente('Fede')
print(x.usuario)
x.usuario = 'Fede el más lindo'
print(x.usuario)