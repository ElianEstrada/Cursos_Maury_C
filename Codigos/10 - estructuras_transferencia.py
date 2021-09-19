# Estructura de transferencias
# transfieren el flujo del código (cambio en el flujo)

# Tipos de Transferencias
# break
# continue
# return

# break -> detener el flujo

# Ejemplo

while (True):
    print("Hola")

    if(True):
        numero = int(input("Ingrese un número: "))

        if (numero > 5):
            break

    print(numero)


print("hola 2")


# # continue -> es saltar una iteración (cuando esta dentro de un ciclo)

# # ejemplo

# lista = [1, None, None, None]

# count = 0
# for elemento in lista:

#     if (elemento != None):
#         count += 1
#         continue

#     lista[count] = 2
#     break

# print("Elemento agregado")
# print(lista)


# return -> esta sentencia es utilizada en funciones
# para retornar un valor (puede ser opcional el valor)
# devuelve el flujo a donde fue llamado    


# Funciones -> es un bloque de código genérico
# que puede ser llamado en cualquier parte del código principal

#sintaxis para funciones
# 'def' nombre_de_funcion '(' [parametros] ')' ':'
# '    ' bloque_codigo
#  
# [] -> indican opcionalidad
# parametros son una lista de variables seperadas por comas
# parametros = nombre, edad

def primera_funcion():
    print("Elian Estrada")

def imprimir_nombre(nombre):
    print(nombre)

    return

#llamadas a función -> nombre_funcion '(' [valores] ')'

nombre_input = input("Ingres nombre: ")

imprimir_nombre(nombre_input)

print("hola mundo")
