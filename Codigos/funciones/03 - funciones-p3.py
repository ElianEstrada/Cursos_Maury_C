# Escribir un programa que solicite una puntación entre 0.0 y 1.0
# Si la puntuación esta fuera de ese rango indicar que es un error
# Si la puntuación esta entre 0.0 y 1.0 muestra la calificación 
# usando la siguiente tabla: 

# >= 0.9 -> sobresaliente
# >= 0.8 -> Notable
# >= 0.7 -> Bien
# >= 0.6 -> suficiente
# < 0.6  -> Insuficiente

def en_rango(puntuacion):
    if (puntuacion < 0.0 or puntuacion > 1.0):
        return False

    return True


def calcular_nota(puntuacion):
    if (puntuacion >= 0.9):
        return "Sobresaliente"
    elif (puntuacion >= 0.8):
        return "Notable"
    elif (puntuacion >= 0.7):
        return "Bien"
    elif (puntuacion >= 0.6):
        return "Suficiente"
    
    return "Insuficiente"


puntuacion = float(input("Ingrese una puntuación: "))

if (en_rango(puntuacion)):
    calcular_nota(puntuacion)

else: 
    print("El rango es invalido, el rango valido es de 0.0 a 1.0")