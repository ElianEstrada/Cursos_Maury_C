# i = 1
# while (i < len(a)):
#     j = 0
#     while (j < len(a) - 1):

#         if (a[j] > a[j + 1]):
#             aux = a[j]
#             a[j] = a[j + 1]
#             a[j + 1] = aux

#         j += 1
#     i += 1

#Funciones en python
#'def' nombre_funcion '(' [lista_parametros] ')' ':'
#'     ' bloque_instrucciones

#Nota:
#[] -> opcionalidad
# lista_parametros -> nombre_variables separadas por ,

#Ejemplo:

def suma(num1, num2):
    print(num1 + num2)

# suma(2, 1.5)
# suma(1, 13)
# suma(15, -114)

#Funciona del metodo de ordenamiento

def intercambio(lista, j):
    aux = lista[j]
    lista[j] = lista[j + 1] 
    lista[j + 1] = aux


def bubblesort(lista, flag): # True -> ascendente, False -> descendente
    i = 1
    while (i < len(lista)):
        j = 0
        while (j < len(lista) - 1):

            if (flag):
                #asc

                if (lista[j] > lista[j + 1]):
                    intercambio(lista, j)
            else:
                #desc
                if (lista[j] < lista[j + 1]):
                    intercambio(lista, j)

            j += 1
        i += 1

    print(lista)


lista1 = [1, 3, 4, 2, 0, 10]
lista2 = [5, 4, 3, 2, 1]
lista3 = [10, 5, 9, 4, 8, 3, 7, 2, 6, 1]

bubblesort(lista1, True)
bubblesort(lista2, True)
bubblesort(lista3, True)

bubblesort(lista1, False)
bubblesort(lista2, False)
bubblesort(lista3, False)
