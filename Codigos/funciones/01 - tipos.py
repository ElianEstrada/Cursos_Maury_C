#Sintaxis de funciones
#Funciones en python
#'def' nombre_funcion '(' [lista_parametros] ')' ':'
#'     ' bloque_instrucciones

#Nota:
#[] -> opcionalidad
# lista_parametros -> nombre_variables separadas por ,

#Hay tres tipos de funciones

# Procedimientos
# Funciones
# Métodos


# Procedimientos
# Es una función que no retorna ningún valor
# es decir su tipo de retorno es nulo.

# Ejemplo de procedimiento

def suma():             # Procedimiento
    print(1 + 2)

suma()
suma()
suma()

def suma(num1, num2):   # Procedimiento
    print(num1 + num2)

suma(1, 4)
suma(2, 6)


# Funciones
# Es una función que retorna un valor.
# es decir que su tipo de retorno es diferente a nulo.

# Ejemplo de función

#'def' nombre_funcion '(' [lista_parametros] ')' ':'
#'     ' bloque_instrucciones

#'def' nombre_funcion '(' [lista_parametros] ')' '->' tipo_dato ':'
#'     ' bloque_instrucciones

#Nota:
#[] -> opcionalidad
# lista_parametros -> nombre_variables separadas por ,
# -> y el tipo_dat es opcional

def operacion_suma(num1, num2):
    return num1 + num2


resultado = operacion_suma(3, 4)
print(resultado)
print(operacion_suma(10, 2))

def operacion_resta(num1, num2) -> int:
    return num1 - num2

print(operacion_resta(3, 1))
print(operacion_resta(3.9, 2.5))
print(operacion_resta("hola", "adios"))


