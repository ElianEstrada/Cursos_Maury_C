from math import pi

def area_cuadrado():
    altura = float(input("Ingrese la altura del cuadrado: "))
    base = float(input("Ingrese la base del cuadrado: "))

    return altura * base

def area_triangulo():
    altura = float(input("Ingrese la altura del triángulo: "))
    base = float(input("Ingrese la base del triángulo: "))

    return (altura * base) / 2

def area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))

    return round(pi * radio ** 2, 2);


def main():

    while (True):
        print("MENU-AREAS");

        print("\n1. Cuadrado\n2. Triangulo\n3. Círculo\n4. Salir");

        opcion = int(input("Ingrese una opción: "))

        if (opcion == 1):
            print(f"El área del cuadrado es: {area_cuadrado()} m²")

        elif(opcion == 2):
            print(f"El área del triángulo es: {area_triangulo()} m²")

        elif(opcion == 3):
            print(f"El área del círculo es: {area_circulo()} m²")

        elif(opcion == 4):
            print("Hasta pronto :)")
            break;
        else: 
            print("Por favor ingrese una opción valida")


if __name__ == '__main__':
    main();