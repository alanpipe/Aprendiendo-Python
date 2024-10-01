#Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

tupla = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

n = int(input("Ingrese el numero de tu letra de l alfabeto: "))

print("La letra correspondiente es: " , tupla[n-1])