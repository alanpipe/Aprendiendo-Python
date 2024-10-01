class A():
    #Metodos
    def __init__(self):
        #Atributos
        self.contador = 0
        #Metodo de instancia
    def incementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador
    
class B():
    #Metodos
    def __init__(self):
        #Atributos
        self.__contador = 0
        #Metodo de instancia
    def incementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador
    
print("Objeeto 1")
#crear objetos
a = A()
print(a.cuenta())
a.incementar()
print(a.cuenta())
print(a.contador) #Mala practica iincorrecta

print("Objeeto 2")
b = B()
print(b.cuenta())
b.incementar()
print(b.cuenta())
print(b.__contador)

