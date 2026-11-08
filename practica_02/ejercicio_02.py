"""
2. Transferencias entre personas (3 ptos)
Requisitos:
• Utilizar la clase Persona del ejercicio anterior y su atributo saldo para simular
transferencias entre dos personas.
• Implementar los métodos necesarios para consultar el saldo y efectuar una transferencia
de dinero de una persona a otra.
• Cada transferencia válida deberá descontar el monto de la persona que envía el dinero y
sumarlo al saldo de quien lo recibe.
• No permitir transferencias con montos no numéricos, menores o iguales a cero, ni
superiores al saldo disponible. Informar al usuario cuando la operación no pueda realizarse
y conservar los saldos sin cambios.
• Demostrar el funcionamiento con dos personas, incluyendo al menos una transferencia
válida y un intento de transferencia rechazado.
"""
class Persona: