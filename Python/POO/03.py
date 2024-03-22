class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calcular_area(self):
        return self.length * self.width


largo = 5
ancho = 3

rectangulo = Rectangle(largo, ancho)
area = rectangulo.calcular_area()

print(f"El área del rectángulo con longitud {largo} y ancho {ancho} es {area}.")
