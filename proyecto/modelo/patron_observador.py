from modelo.decorador_registrar_en_txt import registrar_en_txt

class Subject:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        for observador in self.observadores:
            observador.update()

class TemaBotonera(Subject):
    def __init__(self,):
        self.mensaje_log = None

    def apretar_boton(self, mensaje_log):
        self.mensaje_log = mensaje_log
        self.notificar()

    def get_mensaje_log(self,):
        return self.mensaje_log
    
class Observador:
    def update(self,):
        raise NotImplementedError("Delegación de actualización")

class ObservadorBotoneraLog(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    @registrar_en_txt
    def update(self):
        mensaje_log = self.observado_a.get_mensaje_log()
        print(mensaje_log)
        return mensaje_log
        

if __name__ == '__main__':
    tema1 = TemaBotonera()
    observador_a = ObservadorBotoneraLog(tema1)
    tema1.apretar_boton('Registro de prueba insertado corretamente: 1;2025-04-22;2025-04-22;06:00:00;09:00:00;1;2')