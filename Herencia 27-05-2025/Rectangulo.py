from FiguraGeometrica import FiguraGeometrica
Deberclass Rectangulo(FiguraGeometrica):
    def __init__(self, alto=0, ancho=0):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Rectángulo -> {super().__str__()}, Área: {self.area()}"
