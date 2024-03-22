cantidad_articulos = int(input("Ingrese la cantidad de artículos comprados: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

if cantidad_articulos <= 5:
    descuento = 0  
elif cantidad_articulos < 10:
    descuento = 0.05  
else:
    descuento = 0.08  

precio_unitario_con_descuento = precio_unitario_original * (1 - descuento)

valor_total_a_pagar = cantidad_articulos * precio_unitario_con_descuento

print(f"Valor total a pagar: ${valor_total_a_pagar:.2f}")
