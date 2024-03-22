def encontrar_maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = int(input("Ingresa el primer numero: "))
num2 = int (input("Ingresa el primer numero: "))
num3 = int (input("Ingresa el primer numero: "))

maximo = encontrar_maximo(num1, num2, num3)
print("El máximo de los tres números es:", maximo)

