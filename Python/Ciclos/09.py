
facts = 1

num = int(input("Ingrese un numero para calcular factorial: "))

for i in range (1, num + 1 ):
    facts = facts * i
print(f"El factorial de {num} es {facts}")