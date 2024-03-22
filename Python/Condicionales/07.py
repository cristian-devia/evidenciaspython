print("Seleccione una opción para convertir temperaturas:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Opción: ")

if opcion == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    resultado = (celsius * 1.8) + 32
    print(f"{celsius} grados Celsius son {resultado} grados Fahrenheit")
elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    resultado = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} grados Fahrenheit son {resultado} grados Celsius")
else:
    print("Opción no válida")
