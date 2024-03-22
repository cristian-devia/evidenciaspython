edad = int(input("Ingrese su edad: "))
genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))

if genero == 1:  
    pulsaciones = (220 - edad) / 10
elif genero == 2:  
    pulsaciones = (210 - edad) / 10
else:
    print("Género no válido. Ingrese 1 para femenino o 2 para masculino.")
    pulsaciones = None

if pulsaciones is not None:
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones}")
