# Control de notas
# El usuario indicará la cantidad de notas a ingresar
# posteriomente se solicitarán dichas notas y se promediaran
# para al final mostrar si el alumno esta aprobado o reprobado
# Nota: un alumno será aprobado si su promedio de notas es >= 61

cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: ")) # 5

contador = 1
total_notas = 0

while (contador <= cantidad_notas):
    
    total_notas += float(input(f"Ingrese la nota {contador}: "))

    contador += 1                   # 5

notas_promediadas = total_notas/cantidad_notas


if (notas_promediadas >= 61):
    print(f"El alumno esta aprobado con nota: {notas_promediadas}")
else:
    print(f"El alumno esta reprobado con nota: {notas_promediadas}")