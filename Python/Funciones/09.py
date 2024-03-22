def elementos(lista):
    listasindupli = list(set(lista))
    return listasindupli


lista = [1, 2, 2, 3, 4, 4, 5]
resultado = elementos(lista)
print("Lista original:", lista)
print("Lista sin duplicados:", resultado)
