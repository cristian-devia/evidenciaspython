
nombre = input("¿Cual es su nombre?: ")

edad = int(input("¿Cuantos años tienes?: "))

if  0 <= edad <= 100 :
   if edad >= 18:

    print("Usted es mayor de edad")

   else:
    print("Usted es menor de edad")

else:
    print("Ingresa una edad válida (entre 0 y 100).")



