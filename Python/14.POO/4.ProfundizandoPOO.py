# * Tupla
# **Diccionario

class FabricaTelefono():
    def __init__(self , marca , *colores , **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefono("Alcatel" , "Negro" , "Azul" , m1 = 500 , m2 = 1000 )
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512 # temporal
print(telefono.memoria)

