def registrar_en_txt(funcion):
    def envoltura(*args):
        txt_registro = funcion(*args)
        archivo = open('registro.txt','w')
        archivo.write(txt_registro)
        archivo.close()
        return txt_registro
    return envoltura