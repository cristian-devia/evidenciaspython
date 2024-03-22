numer = int(input("Ingresa la cantidad de números que deseas mostrar: "))

suma = 0
penultimo = 0
ultimo = 1

suma = penultimo + ultimo

print(f"{penultimo} - {ultimo}", end=" ")

for i in range(2, numer):
    siguiente = penultimo + ultimo

    print(f"- {siguiente}", end=" ")

    penultimo = ultimo
    ultimo = siguiente

    suma = suma + siguiente

print(f"\nLa suma de los términos es: {suma}")
