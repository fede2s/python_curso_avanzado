"""
Patron adaptador
Si tengo 2 clases incompatibles ej motor 5v y enchufe de pared
uso una clase adaptador para que motor.enchufar(adaptador(pared()))
me de el voltaje correcto

Patron singleton
solo 1 instancia para una clase. Si uno elige instanciar, ocupa
el mismo espacio que ocupaba la otra instancia. Sirve para usuarios
por ejemplo, para que solo haya uno con la sesión activa

Factory
Si tengo una clase Factory, una clase Auto y una clase Moto,
puedo crear un auto o una moto usando la clase factory. Está en la
mayoría de los frameworks
"""