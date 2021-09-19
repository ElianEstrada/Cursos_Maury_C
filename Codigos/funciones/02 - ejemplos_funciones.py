# El usuario solicita un programa que le permita
# sumar 2 números muchas veces

while (True):

    num1 = int(input("Ingrese el 1er número: "))
    num2 = int(input("Ingrese el 2do número: "))

    print(f"El resultado de sumar {num1} y {num2} es: {num1 + num2}")

    respuesta = input("Desea realizar otra suma? [S/N]: ").lower()

    if (respuesta == 'n'):
        break

print("Vuelva pronto :)")


#con Funciones

def suma(num1, num2):
    print(f"El resultado de sumar {num1} y {num2} es: {num1 + num2}")

while(True):
    num1 = int(input("Ingrese el 1er número: "))
    num2 = int(input("Ingrese el 2do número: "))

    suma(num1, num2)

    respuesta = input("Desea realizar otra suma? [S/N]: ").lower()

    if (respuesta == 'n'):
        break

print("Vuelva pronto :)")


def suma(num1, num2):
    return num1 + num2

print(suma(1, 2))
print(suma(suma(1, 2), 3))
print(suma(suma(1,2), suma(3,4)))
print(suma(suma(suma(1,2), 3), suma(4, 5)))



def suma_n(*args):
    resultado = 0
    for item in args:
        resultado += item

    return resultado

print(suma_n(1, 2, 3, 4))
print(suma_n(1, 2, 3, 4, 5))
print(suma_n(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
