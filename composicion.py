# Clase coordenada
class Coordenada:
    # Método constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Método para mostrar coordenada
    def mostrarCoordenadas(self):
        print("(X):", self.x, ", (Y):", self.y)

# Clase cuadrado
class Cuadrado:
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    # Método para mostrar los vértices 
    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vértices:")
        self.v1.mostrarCoordenadas()
        self.v2.mostrarCoordenadas()
        self.v3.mostrarCoordenadas()
        self.v4.mostrarCoordenadas()

# Método principal
def main():
    # Entrada de datos
    x1 = int(input("Digite el valor de X: "))
    y1 = int(input("Digite el valor de Y: "))

    # Creación de una coordenada
    c1 = Coordenada(x1, y1)
    c1.mostrarCoordenadas()

    # Creación de un cuadrado con 4 coordenadas
    v1 = Coordenada(7, 8)
    v2 = Coordenada(10, 8)
    v3 = Coordenada(7, 5)
    v4 = Coordenada(10, 5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
