
salario = int(input("Salario diario: "))
dias = int(input("Numero de días trabajados: "))


salario_b = salario * dias
pension = salario_b * 0.1
salud = salario_b * 0.15

salario_f = salario_b - pension - salud

print(f"El salario que se debe pagar al empleado es: {salario_f}")

