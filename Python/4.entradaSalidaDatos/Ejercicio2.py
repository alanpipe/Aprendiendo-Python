#Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

#Considere:

#PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

#Donde: P1, P2, P3 : Practicas

#PP: promedio de práctica

#PROM: promedio

#EP: examen parcial

#EF: examen final

p1 = float(input('Ingrese el promedio de la P1: '))
p2 = float(input('Ingrese el promedio de la P2: '))
p3 = float(input('Ingrese el promedio de la P3: '))
EP = float(input('Ingrese el promedio deL examen parcial: '))
EF = float(input('Ingrese el promedio del examen fina: '))

PP = (p1+p2+p3)/3
promedio = (PP+2*EP+3*EF) / 6

print('El promedio de practica del estudiantes es de:\n ', PP, "\n Y el promedio Final es de:\n ", promedio)
