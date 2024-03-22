import math

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False

    return True


numero1 = 17
if es_primo(numero1):
    print(f"{numero1} es un número primo.")
else:
    print(f"{numero1} no es un número primo.")
