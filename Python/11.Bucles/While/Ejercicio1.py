#Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

numero = int(input("Digite un numero para saber su numero: "))

#inizializar contador 
i = 0

while i <= 10 :
    resultado = numero * i
    print("{} x {} = {}".format(numero,i,resultado))
    i += 1

