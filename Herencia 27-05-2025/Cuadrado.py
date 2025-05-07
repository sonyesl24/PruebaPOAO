from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado=0):
        super().__init__(lado, lado)  # ambos lados iguales en un cuadrado

    def area(self):
        return self.alto * self.alto

    def __str__(self):
        return f"Cuadrado -> {super().__str__()}, Área: {self.area()}"
