diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5 , 6 : 7}

print(diccionario)

#eliminar (clave)
diccionario.pop(3)
print(diccionario)

#limpiar diccionario borrar dicionario
'''diccionario.clear()
print(diccionario)'''

#recibe un parametro (llave) y duvuelve valor
print(diccionario.get(2))
#get : traem el valor de la llave 2 (traer valores)

#agregar valores
diccionario.setdefault(4 , 5)
print(diccionario)

#actualizar valores
diccionario.update(diccionario2)
print(diccionario)

#coppy sacar copia
diccionario.copy()
print(diccionario)