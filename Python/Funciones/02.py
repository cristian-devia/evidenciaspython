def area_cuadrado(num1, num2):
    area = num1 * num2
    return area

area = area_cuadrado (5,6)
print("El area del cuadrado es: ", area)


def area_circulo(radio,pi):
    area = pi* (radio**2)
    return area

area = area_circulo(7,3.1416)
print(f"El resultado es: {area}")


def area_triangulo (base, altura):
    area = base * altura/2
    return area
area = area_triangulo(7,8)
print("El area del triangulo es: ", area)

def area_rectangulo (base, altura):
    area = base * altura
    return area
area = area_rectangulo(2,3)
print("El area del rectangulo es: ", area)

def area_rombo (diagonal_mayor, diagonal_menor):
    area=diagonal_mayor*diagonal_menor/2
    return area
area = area_rombo(20,10)
print("El area del rombo es: ",area)

def area_trapecio(base_mayor, base_menor, altura):
    area = (base_mayor+base_menor)*altura/2
    return area

area = area_trapecio (15,9,3)
print("El area del trapecio es: ", area)
 
