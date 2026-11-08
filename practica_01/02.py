#Calcula la nota final ponderada del alumno.
matetica = 17
print("Matemática:",matetica)
ciencia = 14
print("Ciencia:",ciencia)
historia = 15
print("Historia:",historia)

nota_final = ((matetica * 0.40) + (ciencia * 0.30) + (historia * 0.30))
print(f"La nota final es {nota_final:.1f}")

aprobado = nota_final >= 13.0
print(f"¿Aprobado?: {aprobado}")

if aprobado==True:
    print("El estudiante obtuvo una nota final de" ,format(nota_final), "y su estado final es: Aprobado")
else:
    print("El estudiante obtuvo una nota final de" ,format(nota_final), "y su estado final es: Desaprobado" )






