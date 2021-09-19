# Escribir un programa que solicite una puntación entre 0.0 y 1.0
# Si la puntuación esta fuera de ese rango indicar que es un error
# Si la puntuación esta entre 0.0 y 1.0 muestra la calificación 
# usando la siguiente tabla: 

# >= 0.9 -> sobresaliente
# >= 0.8 -> Notable
# >= 0.7 -> Bien
# >= 0.6 -> suficiente
# < 0.6  -> Insuficiente

puntuacion = float(input("Ingrese una puntuación: "))

if (puntuacion < 0.0 or puntuacion > 1.0):
    print("Puntuación fuera de rango, el rango aceptado es de 0.0 - 1.0")

else:

    if (puntuacion >= 0.9):
        print("Sobresaliente")
    elif (puntuacion >= 0.8):
        print("Notable")
    elif (puntuacion >= 0.7):
        print("Bien")
    elif (puntuacion >= 0.6):
        print("Sufiente")
    else:
        print("Insuficiente")
