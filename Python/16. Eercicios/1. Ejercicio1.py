#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre , nota) :
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))

    def Resultados(self):
        if self.nota < 7:
            print("HAS REPROBADO")
        else:
            print(("HAS APROBADO"))

estudiantet1 = Estudiante("Daniel" , 10)
estudiantet1.imprimir()
estudiantet1.Resultados()

estudiante2 = Estudiante("KARLA" , 5)
estudiante2.imprimir()
estudiante2.Resultados()