#Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

import math

def AreaCuadrado(base, altura):
    resultado= base * altura
    return resultado

def AreaCirculo(radio):
    resultado = math.pi * radio **2
    return resultado

print(AreaCuadrado(5 , 5))
print(AreaCirculo(3))
