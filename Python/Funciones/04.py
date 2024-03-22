def multiplicar_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

lista = [8, 2, 3, -1, 7]

resultado = multiplicar_lista(lista)
print("Resultado esperado:", resultado)
