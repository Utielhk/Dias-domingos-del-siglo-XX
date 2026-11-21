import datetime

def contar_domingos():
    contador = 0
    
    # Recorremos los años desde 1900 hasta 2000 (ambos inclusive)
    for anio in range(1900, 2001):
        # Recorremos los 12 meses de cada año
        for mes in range(1, 13):
            # Creamos la fecha para el primer día del mes
            fecha = datetime.date(anio, mes, 1)
            
            # El método weekday() devuelve 6 si es domingo 
            # (0 es Lunes, 1 es Martes, ..., 6 es Domingo)
            if fecha.weekday() == 6:
                contador += 1
                
    return contador

resultado = contar_domingos()
print(f"Total de domingos que cayeron en el primer día de mes: {resultado}")