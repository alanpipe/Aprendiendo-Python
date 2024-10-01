'''Crea un programa que tenga una variable con la cadena
"Te quiero solo como amigo", y muestre la siguiente informacion:
*Imprima los dos primeros caracteres
*Imprima los tres ultimos caracteres
*Imprima dicha cadena cada dos caracteres 
*Dicha cadena en sentido inverso
Imprima la cadena en un sentido y en sentido inverso'''

cadena = "Te quiero solo como amigo"

print(cadena[0 : 2])

print(cadena[-3 : ])
print(cadena[: : 2])
print(cadena[: : -1])
print(cadena + cadena[: : -1])