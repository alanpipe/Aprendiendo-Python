class A():
    #Metodos
    def __init__(self):
        #Atributos
        self._contador = 0
        self._cuenta = 0
    #Metodo Get
    #para que lo llame de forma de atyributo
    @property
    def cuenta(self):
       return self._cuenta
    
    #metodo set
    @cuenta.setter
    def cuenta(self , cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self , contador):
        self._contador = contador
    #Forma correcta
a = A()
print(a.cuenta)
#Modifcar el valor de cuenta 
a.cuenta = 30
print(a.cuenta)
print(a.contador)
a.contador = 25
print(a.contador)