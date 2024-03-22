
print("Tamaño de la pizza:")
print("1. Pequeña ($15,000)")
print("2. Mediana ($24,000)")
print("3. Grande ($36,000)")

tamaño_elegido = int(input("Seleccione el tamaño de la pizza (1/2/3): "))

precio_pequeña = 15000
precio_mediana = 24000
precio_grande = 36000

if tamaño_elegido == 1:
    precio_total = precio_pequeña
    tamaño = "Pequeña"
elif tamaño_elegido == 2:
    precio_total = precio_mediana
    tamaño = "Mediana"
elif tamaño_elegido == 3:
    precio_total = precio_grande
    tamaño = "Grande"
else:
    print("Opción no válida. Por favor, seleccione un tamaño válido.")
    precio_total = 0

if precio_total > 0:
    print(f"Ha seleccionado una pizza {tamaño}. El precio total es: ${precio_total}")
