#class Fabricatelefonos():
 #   marca = "Samsung"

  #  def Elaborarhuaewi(self):
   #     self.marca = "Huawei"

#telefonos = Fabricatelefonos()
#print(telefonos.marca)

#telefonos.Elaborarhuaewi()
#print(telefonos.marca)

class FabricaTelefonos():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei' , 'Negro')
print(telefono.marca)
print(telefono.color)