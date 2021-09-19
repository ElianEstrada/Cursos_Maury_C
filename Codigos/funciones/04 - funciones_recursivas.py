#Una función recursiva no es mas que una función 
# que se llama a si misma dentro de si misma.

def suma(num1):
    if num1 == 0:
        return 0
    return num1 + suma(num1 - 1)

def suma_ciclo(num1):
    resultado = 0
    while num1 != 0:
        resultado = resultado + num1
        num1 -= 1

    return resultado


#print(suma(10000000))
#print(suma_ciclo(10000000))

# 4
# 10

# suma(4)
    # 4 == 0? -> no
    # return 4 + suma(3) -> 4 + 6 = 10 -> return 10

# suma(3)
    # 3 == 0? -> no
    # return 3 + suma(2) -> 3 + 3 = 6 -> return 6

# suma(2)
    # 2 == 0? -> no
    # return 2 + suma(1) -> 2 + 1 = 3 -> return 3

# suma(1)
    # 1 == 0? -> no
    # return 1 + suma(0) -> 1 + 0 = 1 -> return 1

# suma(0)
    # 0 == 0? -> si
    # return 0


def suma(num1):
    if num1 == 0:
        return 0
    return num1 + suma(num1 - 1)

#tips para hacer una función recursiva
# 1. Tener un caso base -> representado por una condición
# 2. Saber como aplicar la recursión

# 5 - 4 - 3 - 2 - 1 - 0
#     4 - 3 - 2 - 1 - 0
#         3 - 2 - 1 - 0
#             2 - 1 - 0
#                 1 - 0
#                     0