#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():
    def __init__(self, llanta, color, precio):
        self.llanta = llanta
        self.color = color
        self. precio = precio
    
class Moto(Fabrica):
    def datos(self):
        print("La canidad de llanta es de: ", self.llanta)
        print("El corlor de la moto es: ", self.color)
        print("El precio de la moto es de: $", self.precio)

class Carro(Fabrica):
    def datos(self):
        print("La canidad de llanta es de: ", self.llanta)
        print("El color del carro es: ", self.color)
        print("El precio del carro es de $: ", self.precio)

moto = Moto(2, "Azul", 2000)
moto.datos()

carro = Carro(4, "Azul",3000)
carro.datos()