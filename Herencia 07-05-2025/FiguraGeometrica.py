class FiguraGeometrica:
    def __init__(self, alto=0, ancho=0):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        self._alto = valor

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor

    def __str__(self):
        return f"Alto: {self._alto}, Ancho: {self._ancho}"
