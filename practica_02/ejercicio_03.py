"""
3. Funciones y manejo de excepciones (3 ptos)
Requisitos:
• Crear una función que solicite al usuario dos valores numéricos por consola y los retorne
para utilizarlos en las operaciones.
• Crear una función que reciba dos valores como parámetros, realice una división y retorne
el resultado.
• Crear una función que reciba dos valores como parámetros, realice una suma y retorne el
resultado.
• Solicitar al usuario cuántos elementos desea registrar (N) y crear una función que reciba
esos datos ingresados por consola, los almacene en una lista y retorne la lista.
• Solicitar al usuario el índice que desea consultar y crear una función que reciba la lista y
dicho índice como parámetros para retornar el elemento correspondiente.
• Controlar los errores provocados por entradas no numéricas, divisiones entre cero,
operaciones entre tipos incompatibles y consultas a posiciones inexistentes de la lista.
• Cuando se produzca un error, mostrar un mensaje descriptivo y permitir un nuevo
intento de la operación correspondiente.
• Utilizar else y finally en al menos una de las operaciones realizadas.
• Ejecutar las funciones creadas utilizando los datos proporcionados por el usuario y
mostrar por consola los resultados de las operaciones correctas. Incluir 3 pruebas con datos
válidos e inválidos.
"""

def valores():
    valor_1 = input("Introduce el primer número: ")
    valor_2 = input("Introduce un segundo número: ")
    print(f"Los valores numéricos registrados son: {valor_1} y {valor_2}")
    return valor_1, valor_2

def division(valor_1, valor_2):
    while True:
        try:
            rslt_div = int(valor_1) / int(valor_2)
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
            while True:
                try:
                    valor_2= float(input("Ingrese un segundo número diferente de cero: "))
                    break
                finally:
                    print("La división se realizo con exito.")
        else:
            print(f"La división es: {rslt_div}")
            return rslt_div

def suma(valor_1,valor_2):
    rslt_sum = int(valor_1) + int(valor_2)
    print(f"La suma es: {rslt_sum}")
    return rslt_sum


def registrar_lista():
    cant = int(input("Introduce el numero de elementos de la lista: "))
    lista = []
    i = 0
    while i < cant:
        elemento = input(f"Ingrese el elemento [{i}]: ")
        lista.append(elemento)
        i += 1
    print(f"\n La lista ingresada es: {lista}")
    return lista


def cnslta_indice(lista):
    indice = int(input("Ingrese un índice válido para consultar: "))
    while True:
        try:
            rslt_cnslta = lista[indice]
            print(f"La posición {indice} de la lista es: {rslt_cnslta}.")
            return rslt_cnslta
        except IndexError:
            print(f"Error: La posición {indice} no existe en la lista. La lista tiene {len(lista)} elementos.")
            try:
                indice = int(input("Ingrese un nuevo índice válido para consultar: "))
            except ValueError:
                print("Error: El índice debe ser un número entero.")






print("\n--Ingrese los números para sumar y dividir--")
n1, n2 = valores()
suma = suma(n1, n2)
division = division(n1, n2)

print("\n\n--Prueba de lista--")
lista = registrar_lista()
cnslta_indice(lista)
