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
    
    @property
    def contador(self):
        return self._contador

    #Forma correcta
a = A()
print(a.cuenta)
print(a.contador)

