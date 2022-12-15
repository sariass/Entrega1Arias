from ejemplo.models import Familiar, Comida, Consola
Familiar(nombre="Pedro", direccion="Avenida Juan 1", f_nacimiento=1955, numero_pasaporte=12345678, edad=67).save()
Familiar(nombre="Juan", direccion="Avenida Pedro 2", f_nacimiento=1998, numero_pasaporte=98765432, edad=24).save()
Familiar(nombre="Valentina", direccion="Avenida Catalina 1", f_nacimiento=2002, numero_pasaporte=91827364, edad=20).save()
Familiar(nombre="Catalina", direccion="Avenida Valentina 2", f_nacimiento= 1925, numero_pasaporte=17483756, edad=97).save()
print("Se cargo con éxito los usuarios de pruebas")

Comida(nombre="Pasta", procedencia="Italia", ingredientes="4").save()
Comida(nombre="Past1", procedencia="Italia2", ingredientes="45").save()
Comida(nombre="Pasta2", procedencia="Italia3", ingredientes="46").save()
print("Se cargo con éxito las comidas de pruebas")

Consola(nombre="Xbox 360", tipo="sobremesa", color="negro/blanco").save()
Consola(nombre="n switch", tipo="portatil", color="rojo/azul").save()
Consola(nombre="playstation 1", tipo="sobremesa", color="gris").save()
print("Se cargo con éxito las consolas de pruebas")