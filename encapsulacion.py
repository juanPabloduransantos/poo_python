# encapsulacion

"""una coordenada en dos dimensiones esta compuesta por dos valores, el valor"""

# clase coordenada

class Coordenada:
    # metodo constructor
    def __init__(self, x, y):
        # atributos privados
        self.__X = x
        self.__Y = y

    # metodos de lectura y escritura de cada atributo
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def setX(self, x):
        self.__X = x

    def setY(self, y):
        self.__Y= y

    # metodo para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y, ")" )
    
# clase Cuadrado

class Cuadrado:

    # metodo constructor
    def __init__(self,v1, v2, v3, v4):
        # atributos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # metodos privados para mostrar los vertices
    def __mostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), ",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), ",", self.__V2.getY(), ")")

    def __mostrarCoordenadaV3(self):
        print("(", self.__V3.getX(), ",", self.__V3.getY(), ")")

    def __mostrarCoordenadaV2(self):
        print("(", self.__V4.getX(), ",", self.__V4.getY(), ")")
    
    # metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

        cuadrado1 = Cuadrado(v1, v2, v3, v4)
        cuadrado1.mostrarVertices()
        
        # que ocurre si el metodo getX() lo hacemos privado: __getX()?
        coordenada = Coordenada(3, 4)
        print("(", coordenada.__getX(), ",", coordenada.getY(), ")")