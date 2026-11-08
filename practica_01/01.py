#1. Usando los tipos de datos y sus conversiones
nombre = "Maria Fuentes"
print("El nombre es:",nombre)
salario = 1700
print("Su salario es: ",salario)
edad = "23"
print("La Edad es: ",edad)
print("El tipo dato Edad es: ",type(edad))
compañia = "ABC s.a.c"


if int(edad) > 30:
    bono = salario * 0.10
    print("Usted tiene un bono de 10% en el mes de diciembre", bono)
else:
    bono = salario * 0.05
    print("Usted tiene un bono de 5% en el mes de diciembre", bono)

bono_final = (salario ** 2) + bono
print(f"El bono final es: {bono_final:.2f}")





