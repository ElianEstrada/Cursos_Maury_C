#lista_parametros

def suma(num1, num2):
    print(num1 + num2)

# Valores por defecto
# nombre_parametro '=' valor_defecto

def suma_defecto(num1, num2 = 10):

    if num1 == 20:
        print("hola")

    return num1 + num2

print(suma_defecto(2, 20)) #-> 22
print(suma_defecto(num2 = 20)) # -> 50
print(suma_defecto(num2 = 10, num1 = 20))