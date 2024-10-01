diccionario = {'Nombre' : "Alan" , 'Apellido' : "Cervantes" , " Estatura" : 1.90}

print(diccionario)

#Mostrar solo llavey (clave)
print(diccionario.keys())

#Mostrar solo valores del diccionarios
print(diccionario.values())

#Mostrar el valor de alguna  clave
print(diccionario[" Estatura"])

#Agregar una nueva clave y su valor
diccionario["Peso"] = "60 kg"
print(diccionario)

#Modificar el valor ya existente
diccionario["Nombre"] = "Fidel"
print(diccionario)