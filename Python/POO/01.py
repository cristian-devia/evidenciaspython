import datetime

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def tiene_restriccion(self, fecha):
       
        ultimo_digito = int(self.placa[-1])
        
        
        dia_semana = fecha.weekday()
        
       
        if dia_semana == 0: 
            return ultimo_digito in [1, 2]
        elif dia_semana == 1:  
            return ultimo_digito in [3, 4]
        elif dia_semana == 2: 
            return ultimo_digito in [5, 6]
        elif dia_semana == 3:  
            return ultimo_digito in [7, 8]
        elif dia_semana == 4:  
            return ultimo_digito in [9, 0]
        else:
            return False  

placa_vehiculo = "ABC092"
fecha_actual = datetime.datetime.now()  

vehiculo = Vehiculo(placa_vehiculo)
tiene_restriccion = vehiculo.tiene_restriccion(fecha_actual)

if tiene_restriccion:
    print(f"El vehículo con placa {placa_vehiculo} tiene restricción por pico y placa hoy.")
else:
    print(f"El vehículo con placa {placa_vehiculo} no tiene restricción por pico y placa hoy.")
