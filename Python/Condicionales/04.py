
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:

    mayor = num1
    menor = num2

elif num1 < num2:
    
    mayor = num2
    menor = num1

print(f"El numero mayor es el {mayor} y el numero menor es el {menor}")    