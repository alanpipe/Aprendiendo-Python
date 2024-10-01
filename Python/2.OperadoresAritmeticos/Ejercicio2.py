#Una jugueteria tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, asi que deben calcular el peso de los payasos y muñecas que saldrán  en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Un cliente frecuente pide la cantidad  de 23 payasos y 54 muñecas, realiza un programa que  muestre el peso total de toda la venta.

#Pista:Suponiendo que un cliente pide 5 payasos y 3 muñecas,la juguetería debería hacer la multiplicacion de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de  peso, se debe sumar.

#23 payasos-> 112g
# 54 munecas-> 75g

payasos = 23
munecas = 54


print("El peso total es de: " , ((payasos * 112) + (munecas * 75)))