class Ave:
    def __init__(self, nombre, habitat):
        self.nombre = nombre
        self.habitat = habitat

    def volar(self):
        print(f"{self.nombre} Habilidad de vuelo.")

class Pajaro(Ave):
    def cantar(self):
        print(f"{self.nombre} Come gusanos.")

class Aguila(Ave):
    def cazar(self):
        print(f"{self.nombre} Es buen cazador.")


gorrion = Pajaro("Gorrión", "Jardín")
aguila_calva = Aguila("Águila Calva", "Montañas")

gorrion.volar()
gorrion.cantar()

aguila_calva.volar()
aguila_calva.cazar()
