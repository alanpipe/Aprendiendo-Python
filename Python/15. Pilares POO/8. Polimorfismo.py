class Animales():
     def __init__(self , mensaje):
         self.mensaje = mensaje
    
     def Hablas(self):
        print(self.mensaje)

class Perro(Animales):
    def hablas(self):
        print("Yo hago Guaa!")

class Pez(Animales):
    def hablas(self):
        print("Yo no hablo!")

perro = Perro("Guaa!")
perro.hablas()

animal = Animales("Miauu")
animal.Hablas()

pez = Pez("BBRR")
pez.hablas()