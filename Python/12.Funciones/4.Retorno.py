'''# def <nombrfe funcion> ():
        <sentencias>
        return'''

def entero():
    print("Este es un numero entero: ")
    return 10
def decimal():
    print("Este un numero decimal: ")
    return  90.99
def frase():
    return "Mi nombre es Alan Cervantes"
def asignacion():
    return 1 , 2 , 3 , 4 , 5


print(entero())
print(decimal())
print(frase())

a , b , c ,d ,e = asignacion()
print(a)
print(b)