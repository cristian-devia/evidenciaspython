
while True:
    print("\nMenú")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Rombo")
    print("6. Trapecio")
    print("7. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5/6/7): ")

    if opcion == "1":
        lado = float(input("Ingresa la longitud del lado del cuadrado: "))
        area = lado * lado
        print(f"El área del cuadrado es: {area}")
    elif opcion == "2":
        base = float(input("Ingresa la longitud de la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    elif opcion == "3":
        base = float(input("Ingresa la longitud de la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif opcion == "4":
        radio = float(input("Ingresa el radio del círculo: "))
        area = 3.14159265359 * radio**2
        print(f"El área del círculo es: {area}")
    elif opcion == "5":
        diagonal_mayor = float(input("Ingresa la longitud de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la longitud de la diagonal menor del rombo: "))
        area = (diagonal_mayor * diagonal_menor) / 2
        print(f"El área del rombo es: {area}")
    elif opcion == "6":
        base_mayor = float(input("Ingresa la longitud de la base mayor del trapecio: "))
        base_menor = float(input("Ingresa la longitud de la base menor del trapecio: "))
        altura = float(input("Ingresa la altura del trapecio: "))
        area = ((base_mayor + base_menor) * altura) / 2
        print(f"El área del trapecio es: {area}")
    elif opcion == "7":
        print("Adios champion")
        break
    else:
        print("Opción no válida.")
