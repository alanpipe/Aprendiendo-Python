class FabricaTelefonos():
    marca = "HHuawei"
    color = "Negro"
    memoriaRam= 32
    almacenamiento = 128

#Metodo instancia (propi crearlo)
    def llamar(self , mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")

#objeto 1
telefono = FabricaTelefonos()

telefono.marca
telefono.color
telefono.marca
telefono.almacenamiento

print(telefono.llamar("Hola, Con quien Hablo?"))
telefono.escucharMusica()