#4. Registro de participantes con listas
participantes = []
participante1 = "Luis"
participante2 = "Mariana"
participante3 = "Pedro"
participantes.append(participante1)
participantes.append(participante2)
participantes.append(participante3)

print("Los participantes son: ",participantes)
new_participante = "Rita"
print("El nuevo participante de la posición 2 es: ",new_participante)
participantes.insert(1,new_participante)
print("Nueva lista de participantes: ",participantes)
participantes.remove("Luis")
participantes.insert(0,"Luisa")
print("La lista actualizada de participantes: ",participantes)
participantes.remove("Pedro")
print("La lista final es: ",participantes)
print("La cantidad de participantes es: ",len(participantes))


