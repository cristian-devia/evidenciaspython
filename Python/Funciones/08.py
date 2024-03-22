def contar_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0

    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1

    return mayusculas, minusculas


cadena = "Figuro Pae"
mayusculas, minusculas = contar_mayusculas_minusculas(cadena)
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")
