"""
Un descriptor es como la propiedad pero un poco
mas general. El descriptor me permite declarar
una clase para agregar informacion o una accion
cuando seteo, llamo o borro un atributo

"""

class DescriptorUsuario:
    """Documentacion descriptor usuario"""
    def __get__(self,instance, owner):
        print('Lógica para recuperar el usuario')
        return instance._usuario.upper()
    
    def __set__(self,instance,valor):
        print('Modificar usario')
        instance._usuario = valor
        
    def __delete__(self,instance):
        print('Remover el usuario')
        del instance._usuario

class Cliente:
    def __init__(self, usuario):
        self._usuario = usuario

    usuario = DescriptorUsuario()

cliente1= Cliente('Fede')
print(cliente1.usuario)
cliente1.usuario = 'Fede el más lindo'
print(cliente1.usuario)


"""Descriptor dentro de una clase
Para casos en que el descriptor no se comparte
con otras clases, puedo declararlo adentro de la
clase que lo utiliza"""

class DescriptorUsuario:
    """Documentacion descriptor usuario"""
    def __get__(self,instance, owner):
        print('Lógica para recuperar el usuario')
        return instance._usuario.upper()
    
    def __set__(self,instance,valor):
        print('Modificar usario')
        instance._usuario = valor
        
    def __delete__(self,instance):
        print('Remover el usuario')
        del instance._usuario

class Cliente:
    def __init__(self, usuario):
        self._usuario = usuario

    class DescriptorUsuario:
        """Documentacion descriptor usuario"""
        def __get__(self,instance, owner):
            print('Lógica para recuperar el usuario')
            return instance._usuario.upper()
        
        def __set__(self,instance,valor):
            print('Modificar usario')
            instance._usuario = valor
            
        def __delete__(self,instance):
            print('Remover el usuario')
            del instance._usuario

    usuario = DescriptorUsuario()

cliente1= Cliente('Fede')
print(cliente1.usuario)
cliente1.usuario = 'Fede el más lindo'
print(cliente1.usuario)