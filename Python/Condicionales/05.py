
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

prom = nota1 + nota2 + nota3 / 3

if prom >= 3.0:
    print ("El alumno aprobó")
else :
    print("El alumno no aprobo")