"""
1. Registro de personas (4 ptos)
Requisitos:
• Crear una clase Persona con los atributos nombre, edad, saldo y nacionalidad. La
nacionalidad tendrá como valor inicial “Peruana”.
• Implementar un método que permita registrar el nombre y la edad de una persona
mediante la consola. Si la edad ingresada no es un número entero válido o es negativa,
informar el problema y solicitar nuevamente el dato.
• Implementar un método cumpleaños que incremente la edad en un año cada vez que se
invoque.
• Crear como mínimo dos objetos de la clase Persona, utilizar el método cumpleaños y
mostrar las edades actualizadas.
• Registrar el momento de creación de cada persona y mostrar, mediante una función, la
fecha y hora de registro con precisión de minutos.
"""
from datetime import datetime
class Persona:
    def __init__(self):
        self.nombre = "" #input("Ingresa su nombre: ")
        self.edad = 0 #"input("Ingresa su edad: ")
        self.saldo = 0
        self.nacionalidad = "Peruana"
        self.fecha_registro = datetime.now()

    def registro(self):
        self.nombre = input("Ingrese su nombre: ")

        while True:
            try:
                edad = int(input(f"Ingrese su edad: "))
                if edad < 0:
                    print("   Error: Su edad no puede ser negativa, por favor intente nuevamente.")
                else:
                    self.edad = edad
                    break 
            except ValueError:
                print("Error: Debe ingresar su edad, por favor intente nuevamente.")

        print(f" Se registro a {self.nombre}, su edad es {self.edad} años.")

    def cumpleanos(self):
        self.edad += 1
        print(f" Su proxima edad será: {str(self.edad)}")

    def fecha_hora(self):
        fecha_formateada = self.fecha_registro.strftime("%Y-%m-%d %H:%M")
        print(f" El registro de: {self.nombre} se realizo el : {fecha_formateada}")




print("--- REGISTRO DE LA PRIMERA PERSONA ---")
persona1 = Persona()
persona1.registro()
persona1.cumpleanos()
persona1.fecha_hora()
print("--- REGISTRO DE LA SEGUNDA PERSONA ---")
persona2 = Persona()
persona2.registro()
persona2.cumpleanos()
persona2.fecha_hora()


